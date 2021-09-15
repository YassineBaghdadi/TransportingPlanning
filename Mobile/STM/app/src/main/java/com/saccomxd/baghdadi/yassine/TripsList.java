package com.saccomxd.baghdadi.yassine;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.annotation.SuppressLint;
import android.content.Context;
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

        String b = "yassine";
        userName = pref.getString("user", null);
        System.out.println(userName);
        trips = dbref.child(userName).child("trips");
        trips.addValueEventListener(new ValueEventListener() {
            @SuppressLint("NotifyDataSetChanged")
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
//

                for(DataSnapshot dataSnapshot : snapshot.getChildren()){
                    String trip = dataSnapshot.getKey();
                    trips_dates.add(trip);

                }
                Toast.makeText(getApplicationContext(), "welcome back Mr "+userName+" you have "+snapshot.getChildrenCount()+" Trips .", Toast.LENGTH_SHORT).show();
                myAdapter.notifyDataSetChanged();
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });
//        Toast.makeText(getApplicationContext(), "You have " + snapshot.getChildrenCount() + " trips .", Toast.LENGTH_SHORT).show();
//        Toast.makeText(getApplicationContext(), "welcome back Mr "+userName+" you have ", Toast.LENGTH_SHORT).show();


    }


}