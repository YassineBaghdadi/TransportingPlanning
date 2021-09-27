package com.saccomxd.baghdadi.yassine;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout;

import android.Manifest;
import android.annotation.SuppressLint;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.location.LocationManager;
import android.os.Bundle;
import android.os.Handler;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;

public class TripsList extends AppCompatActivity {
    ArrayList<String> trips_dates;
    RecyclerView recyclerView;
    MyAdapter myAdapter;
    ArrayList<trip> list;
    private String userName;
    private int trips_count;
    FirebaseDatabase db;
    DatabaseReference dbref, trips;
    SharedPreferences pref;
    SharedPreferences.Editor editor;
    private LocationManager locationManager;

    Handler handler = new Handler();
    Runnable runnable;
    int delay = 10000;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.trip_list_layout);

        recyclerView = findViewById(R.id.myrec);
        recyclerView.setHasFixedSize(true);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        db = FirebaseDatabase.getInstance();
        dbref = db.getReference("drivers");
        list = new ArrayList<>();
        trips_dates = new ArrayList<String>();
        myAdapter = new MyAdapter(this, trips_dates);
        recyclerView.setAdapter(myAdapter);
        pref = getApplicationContext().getSharedPreferences("var", Context.MODE_PRIVATE);
        editor = pref.edit();
//        ActivityCompat.requestPermissions(this, new String[] {Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION, Manifest.permission.ACCESS_NETWORK_STATE}, 1);
        String b = "yassine";
        userName = pref.getString("user", null);
        System.out.println(userName);
        trips = dbref.child(userName).child("trips");

        handler.postDelayed(runnable = new Runnable() {
            public void run() {

                handler.postDelayed(runnable, delay);
                variables v = new variables();
                dbref.child(userName).child("currentloc").setValue(v.getLocation(getApplicationContext()));
            }
        }, delay);
        refresh();
        SwipeRefreshLayout srl = findViewById(R.id.swipeRefresh);
        srl.setOnRefreshListener(new SwipeRefreshLayout.OnRefreshListener() {
            @Override
            public void onRefresh() {
                refresh();
                srl.setRefreshing(false);
            }
        });
//        handler.removeCallbacks(runnable);

//        trips.

//        Toast.makeText(getApplicationContext(), "You have " + list.size() + " trips .", Toast.LENGTH_SHORT).show();
//        Toast.makeText(getApplicationContext(), "welcome back Mr "+userName+" you have ", Toast.LENGTH_SHORT).show();


    }
    private void refresh(){
        trips.addListenerForSingleValueEvent(new ValueEventListener() {
            @SuppressLint("NotifyDataSetChanged")
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                trips_dates.clear();

                for(DataSnapshot dataSnapshot : snapshot.getChildren()){
                    String trip = dataSnapshot.getKey();
                    trips_dates.add(trip);

                }

                myAdapter.notifyDataSetChanged();
//                recyclerView.notifyAll();
                Toast.makeText(getApplicationContext(), "welcome back Mr "+userName+" you have "+trips_dates.size()+" Trips .", Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });
    }
//
    @Override
    public void onBackPressed() {
        super.onBackPressed();
        startActivity(new Intent(this, login.class));
        finish();
    }

    @Override
    protected void onPause() {
        super.onPause();
        finish();
    }
    @Override
    protected void onResume() {
        super.onResume();
        locationManager = (LocationManager) getSystemService(LOCATION_SERVICE);
        if (!locationManager.isProviderEnabled(LocationManager.GPS_PROVIDER)){
            AlertDialog.Builder alertDialogBuilder = new AlertDialog.Builder(this);
            alertDialogBuilder.setMessage("GPS is disabled in your device. Would you like to enable it?")
                    .setCancelable(false)
                    .setPositiveButton("Goto Settings Page To Enable GPS",
                            new DialogInterface.OnClickListener(){
                                public void onClick(DialogInterface dialog, int id){
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