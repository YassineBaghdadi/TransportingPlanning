package com.saccomxd.baghdadi.yassine;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.Manifest;
import android.annotation.SuppressLint;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
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

        trips.addValueEventListener(new ValueEventListener() {
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
//        Toast.makeText(getApplicationContext(), "You have " + list.size() + " trips .", Toast.LENGTH_SHORT).show();
//        Toast.makeText(getApplicationContext(), "welcome back Mr "+userName+" you have ", Toast.LENGTH_SHORT).show();


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
}