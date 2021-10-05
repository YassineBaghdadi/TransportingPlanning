package com.saccomxd.baghdadi.yassine;

import android.Manifest;
import android.annotation.SuppressLint;
import android.app.Activity;
import android.app.Dialog;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.location.LocationManager;
import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.view.Window;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.core.app.ActivityCompat;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.text.SimpleDateFormat;
import java.time.temporal.TemporalAccessor;
import java.util.Date;
import java.util.List;
import java.util.Locale;

public class dialog_trips {
    FirebaseDatabase fDb;
    DatabaseReference db;
    private String type;
    boolean started, finiched;
    int startedCounterKM;

    Location gps_loc;
    Location network_loc;
    Location final_loc;
    double longitude;
    double latitude;
    String userCountry, userAddress, active_trip;


    Handler handler = new Handler();
    Runnable runnable;
    int delay = 1000;
    String TheTrip;

    public void showdialog(Context activity) {
//        final Dialog dialog = new Dialog(activity, R.style.DialogAnimation);
        final Dialog dialog = new Dialog(activity);
        dialog.requestWindowFeature(Window.FEATURE_NO_TITLE);
        dialog.setCancelable(true);
        dialog.setContentView(R.layout.custom_dialog);
//        dialog.setCanceledOnTouchOutside(true);
        SharedPreferences sharedPreferences = activity.getSharedPreferences("var", Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPreferences.edit();
        TextView action = (TextView) dialog.findViewById(R.id.action);
        EditText counter = (EditText) dialog.findViewById(R.id.counter);
        active_trip = "0";
        TextView viewbtn = (TextView) dialog.findViewById(R.id.view);
        fDb = FirebaseDatabase.getInstance();
        TheTrip = sharedPreferences.getString("trip", null);
        @SuppressLint("SimpleDateFormat") SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        Date date = new Date();
        String datetime = formatter.format(date);


        Toast.makeText(activity, TheTrip.split(":")[0] + " And "+datetime.split(":")[0], Toast.LENGTH_SHORT).show();
        //TODO : stoped here
        if (TheTrip.split(":")[0].equals(datetime.split(":")[0].toString()) ){


            db = fDb.getReference("drivers").child(sharedPreferences.getString("user", null)).child("trips").child(sharedPreferences.getString("trip", null));
            db.addListenerForSingleValueEvent(new ValueEventListener() {
                @Override
                public void onDataChange(@NonNull DataSnapshot snapshot) {

                    if (snapshot.hasChild("startcounter") && snapshot.hasChild("stopcounter")) {
                        action.setText("DONE");
                        action.setBackgroundResource(R.drawable.rouded_corner_gray);
                        started = true;
                        finiched = true;
                        action.setEnabled(false);
                        counter.setEnabled(false);
//                    viewbtn.setEnabled(false);
                    }

                    if (!snapshot.hasChild("stopcounter") && !snapshot.hasChild("startcounter")) {
                        action.setText("START");
                        action.setBackgroundResource(R.drawable.rouded_corner_green);
                        started = false;
                        finiched = false;
                    }
                    if (snapshot.hasChild("startcounter") && !snapshot.hasChild("stopcounter")) {
                        startedCounterKM = Integer.parseInt(snapshot.child("startcounter").getValue().toString());
                        action.setText("STOP");
                        action.setBackgroundResource(R.drawable.rouded_corner_red);
                        started = true;
                        finiched = false;

                    }
                }

                @Override
                public void onCancelled(@NonNull DatabaseError error) {

                }
            });

        }
        else {
            action.setText("ERR");
            action.setBackgroundResource(R.drawable.rouded_corner_gray);
            action.setEnabled(false);
        }



        viewbtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                activity.startActivity(new Intent(activity, AgentsList.class));
                dialog.dismiss();
            }
        });

        action.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (counter.getText().toString().matches("")) {
                    Toast.makeText(activity, "Put counter KM ...", Toast.LENGTH_SHORT).show();
                } else {
                    @SuppressLint("SimpleDateFormat") SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
                    Date date = new Date();
                    String datetime = formatter.format(date);

                    if (started) {
                        if (Integer.parseInt(counter.getText().toString()) > startedCounterKM){
                            db.child("stopcounter").setValue(counter.getText().toString());
                            db.child("stoptime").setValue(datetime.split("\\s+")[1]);
                            db.child("stoploc").setValue(getLocation(activity));
                            editor.putString("activetrip", "0");
                            fDb.getReference("drivers").child(sharedPreferences.getString("user", null)).child("activetrip").setValue("0");

                            editor.apply();
                            activity.startActivity(new Intent(activity, TripsList.class));
                            dialog.dismiss();

                        }else {
                            Toast.makeText(activity, "The Stop Counter has to be Greater than The Start one ", Toast.LENGTH_SHORT).show();
                        }
                    } else {
                        editor.putString("activetrip", sharedPreferences.getString("trip", null));
                        fDb.getReference("drivers").child(sharedPreferences.getString("user", null)).child("activetrip").setValue(sharedPreferences.getString("trip", null));
                        editor.apply();
                        db.child("startcounter").setValue(counter.getText().toString());
                        db.child("starttime").setValue(datetime.split("\\s+")[1]);
                        db.child("startloc").setValue(getLocation(activity));

                        activity.startActivity(new Intent(activity, AgentsList.class));
                        dialog.dismiss();


                    }

                }


            }
        });


        dialog.show();

    }



    public String getLocation(Context context){

        LocationManager locationManager = (LocationManager) context.getSystemService(Context.LOCATION_SERVICE);

        if (ActivityCompat.checkSelfPermission(context, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED
                && ActivityCompat.checkSelfPermission(context, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED
                && ActivityCompat.checkSelfPermission(context, Manifest.permission.ACCESS_NETWORK_STATE) != PackageManager.PERMISSION_GRANTED) {

            return "error";
        }

        try {

            gps_loc = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);
            network_loc = locationManager.getLastKnownLocation(LocationManager.NETWORK_PROVIDER);

        } catch (Exception e) {
            e.printStackTrace();
        }
        if (gps_loc != null) {
            final_loc = gps_loc;
            latitude = final_loc.getLatitude();
            longitude = final_loc.getLongitude();
        }
        else if (network_loc != null) {
            final_loc = network_loc;
            latitude = final_loc.getLatitude();
            longitude = final_loc.getLongitude();
        }
        else {
            latitude = 0.0;
            longitude = 0.0;
        }
//        ActivityCompat.requestPermissions(this, new String[] {Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION, Manifest.permission.ACCESS_NETWORK_STATE}, 1);
        try {

            Geocoder geocoder = new Geocoder(context, Locale.getDefault());
            List<Address> addresses = geocoder.getFromLocation(latitude, longitude, 1);
            if (addresses != null && addresses.size() > 0) {
                userCountry = addresses.get(0).getCountryName();
                userAddress = addresses.get(0).getAddressLine(0);
                Toast.makeText(context, "Latitude : "+addresses.get(0).getLatitude()+" - Longitude : "+addresses.get(0).getLongitude(), Toast.LENGTH_SHORT).show();
//                editor.putString("loc", addresses.get(0).getLatitude()+","+addresses.get(0).getLongitude());
                return addresses.get(0).getLatitude()+","+addresses.get(0).getLongitude();


            }
            else {
                userCountry = "Unknown";

            }

        } catch (Exception e) {
            e.printStackTrace();
        }
        return "error";
    }

}