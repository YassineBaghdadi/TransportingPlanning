package com.saccomxd.baghdadi.yassine;

import static android.Manifest.permission.ACCESS_COARSE_LOCATION;
import static android.content.ContentValues.TAG;

import android.Manifest;
import android.annotation.SuppressLint;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.location.LocationRequest;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.provider.Settings;
import android.util.Log;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout;

import com.google.android.gms.location.FusedLocationProviderClient;
import com.google.android.gms.location.LocationCallback;
import com.google.android.gms.location.LocationResult;
import com.google.android.gms.location.LocationServices;
import com.google.android.gms.location.LocationSettingsRequest;
import com.google.android.gms.location.SettingsClient;
import com.google.android.material.snackbar.Snackbar;
import com.google.firebase.database.ChildEventListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import org.w3c.dom.Comment;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Locale;

public class AgentsList extends AppCompatActivity {
    ArrayList<agent> agentsNames;
    RecyclerView recyclerView;
    AgentAdapter myAdapter;

    String tripName, userName;
    SharedPreferences pref;
    SharedPreferences.Editor editor;

    private int trips_count;
    FirebaseDatabase db;
    DatabaseReference dbref, agents;

    private LocationManager locationManager;
    private LocationListener listener;

    // location last updated time
    private String mLastUpdateTime;

    // bunch of location related apis
    private FusedLocationProviderClient mFusedLocationClient;
    private SettingsClient mSettingsClient;
    private LocationRequest mLocationRequest;
    private LocationSettingsRequest mLocationSettingsRequest;
    private LocationCallback mLocationCallback;
    private Location mCurrentLocation;

    Location gps_loc;
    Location network_loc;
    Location final_loc;
    double longitude;
    double latitude;
    String userCountry, userAddress;


    Handler handler = new Handler();
    Runnable runnable;
    int delay = 500;

    String active_trip;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.agent_list_layout);
//        ActivityCompat.requestPermissions(this, new String[] {Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION, Manifest.permission.ACCESS_NETWORK_STATE}, 1);
        recyclerView = findViewById(R.id.agent_yrec);
        recyclerView.setHasFixedSize(true);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));


//        list = new ArrayList<agents>();
        agentsNames = new ArrayList<>();
        myAdapter = new AgentAdapter(agentsNames, this);
        recyclerView.setAdapter(myAdapter);
        pref = this.getSharedPreferences("var", Context.MODE_PRIVATE);
        editor = pref.edit();
        userName = pref.getString("user", null);
        tripName = pref.getString("trip", null);
        db = FirebaseDatabase.getInstance();
        dbref = db.getReference("drivers");
//        LocationManager locationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
        refresh();
        SwipeRefreshLayout srl = findViewById(R.id.srl);
        srl.setOnRefreshListener(new SwipeRefreshLayout.OnRefreshListener() {
            @Override
            public void onRefresh() {
                refresh();
                srl.setRefreshing(false);
            }
        });




//        active_trip = pref.getString("activetrip", null);

        dbref.child(userName).addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                if (snapshot.hasChild("activetrip")){
                    active_trip = String.valueOf(snapshot.child("activetrip").getValue());
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });




        handler.postDelayed(runnable = new Runnable() {
            public void run() {

                handler.postDelayed(runnable, delay);
                if (!active_trip.equals("0")) {

//                    if (ActivityCompat.checkSelfPermission(getApplicationContext(), Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED
//                            && ActivityCompat.checkSelfPermission(getApplicationContext(), Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED
//                            && ActivityCompat.checkSelfPermission(getApplicationContext(), Manifest.permission.ACCESS_NETWORK_STATE) != PackageManager.PERMISSION_GRANTED) {
//
//                        ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION, Manifest.permission.ACCESS_NETWORK_STATE, Manifest.permission.CALL_PHONE}, 1);
//                    }



                    variables v = new variables();
                    @SuppressLint("SimpleDateFormat") SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
                    Date date = new Date();
                    String datetime = formatter.format(date);
                    dbref.child(userName).child("trips").child(active_trip).child("tracking").child(datetime.split("\\s+")[1]).setValue(v.getLocation(getApplicationContext()));
                }
            }
        }, delay);
//        handler.removeCallbacks(runnable);

//
//        LocationManager locationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
//
//        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED
//                && ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED
//                && ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_NETWORK_STATE) != PackageManager.PERMISSION_GRANTED) {
//
//            return;
//        }
//
//        try {
//
//            gps_loc = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);
//            network_loc = locationManager.getLastKnownLocation(LocationManager.NETWORK_PROVIDER);
//
//        } catch (Exception e) {
//            e.printStackTrace();
//        }
//        if (gps_loc != null) {
//            final_loc = gps_loc;
//            latitude = final_loc.getLatitude();
//            longitude = final_loc.getLongitude();
//        }
//        else if (network_loc != null) {
//            final_loc = network_loc;
//            latitude = final_loc.getLatitude();
//            longitude = final_loc.getLongitude();
//        }
//        else {
//            latitude = 0.0;
//            longitude = 0.0;
//        }
//        ActivityCompat.requestPermissions(this, new String[] {Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION, Manifest.permission.ACCESS_NETWORK_STATE}, 1);
//        try {
//
//            Geocoder geocoder = new Geocoder(this, Locale.getDefault());
//            List<Address> addresses = geocoder.getFromLocation(latitude, longitude, 1);
//            if (addresses != null && addresses.size() > 0) {
//                userCountry = addresses.get(0).getCountryName();
//                userAddress = addresses.get(0).getAddressLine(0);
//                Toast.makeText(getApplicationContext(), "Latitude : "+addresses.get(0).getLatitude()+" - Longitude : "+addresses.get(0).getLongitude(), Toast.LENGTH_SHORT).show();
//                editor.putString("loc", String.valueOf(addresses.get(0).getLatitude())+","+addresses.get(0).getLongitude());
//
//
//            }
//            else {
//                userCountry = "Unknown";
//
//            }
//
//        } catch (Exception e) {
//            e.printStackTrace();
//        }


    }

    private void refresh() {

        db = FirebaseDatabase.getInstance();
        agents = dbref.child(userName).child("trips").child(tripName).child("agents");
//        agentsNames.clear();
        agents.addListenerForSingleValueEvent(new ValueEventListener() {
            @SuppressLint("NotifyDataSetChanged")
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
//                Toast.makeText(getApplicationContext(), "You have " + snapshot.getChildrenCount() + " Agents in this trip .", Toast.LENGTH_SHORT).show();
                agentsNames.clear();
//                System.out.println("data from Firebase : "+snapshot.getValue());

                for (DataSnapshot dataSnapshot : snapshot.getChildren()) {
//                    agent agent = dataSnapshot.getValue(agent.class);
//                    System.out.println(snapshot.getValue());
                    agentsNames.add(dataSnapshot.getValue(agent.class));
//                        myAdapter = new AgentAdapter(agentsNames, getApplicationContext());
//                        recyclerView.setAdapter(myAdapter);
//                    System.out.println("data from Firebase : " + dataSnapshot.child("presence").getValue());


                }
                myAdapter.notifyDataSetChanged();
//                recyclerView.notifyAll();
            }


            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                Toast.makeText(getApplicationContext(), "Loading Data Error : " + error, Toast.LENGTH_SHORT).show();
            }

        });


//        agents.addChildEventListener(new ChildEventListener() {
//            @Override
//            public void onChildAdded(@NonNull DataSnapshot snapshot, @Nullable String previousChildName) {
//
//            }
//
//            @Override
//            public void onChildChanged(@NonNull DataSnapshot snapshot, @Nullable String previousChildName) {
//
//            }
//
//            @Override
//            public void onChildRemoved(@NonNull DataSnapshot snapshot) {
//
//            }
//
//            @Override
//            public void onChildMoved(@NonNull DataSnapshot snapshot, @Nullable String previousChildName) {
//
//            }
//
//            @Override
//            public void onCancelled(@NonNull DatabaseError error) {
//
//            }
//        });
    }


    @Override
    public void onBackPressed() {
        super.onBackPressed();
        startActivity(new Intent(this, TripsList.class));
        finish();
    }

    @Override
    protected void onPause() {
        super.onPause();
        Toast.makeText(getApplicationContext(), "Paused", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onResume() {
        super.onResume();
        locationManager = (LocationManager) getSystemService(LOCATION_SERVICE);
        if (!locationManager.isProviderEnabled(LocationManager.GPS_PROVIDER)) {
            AlertDialog.Builder alertDialogBuilder = new AlertDialog.Builder(this);
            alertDialogBuilder.setMessage("GPS is disabled in your device. Would you like to enable it?")
                    .setCancelable(false)
                    .setPositiveButton("Goto Settings Page To Enable GPS",
                            new DialogInterface.OnClickListener() {
                                public void onClick(DialogInterface dialog, int id) {
                                    Intent callGPSSettingIntent = new Intent(
                                            android.provider.Settings.ACTION_LOCATION_SOURCE_SETTINGS);
                                    startActivity(callGPSSettingIntent);


                                }
                            });

            AlertDialog alert = alertDialogBuilder.create();
            alert.show();

        }
    }

}