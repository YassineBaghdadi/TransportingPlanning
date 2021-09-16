package com.saccomxd.baghdadi.yassine;

import static android.content.ContentValues.TAG;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.google.firebase.database.ChildEventListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import org.w3c.dom.Comment;

import java.util.ArrayList;

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

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.agent_list_layout);

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

        refresh();
    }


    private void refresh() {

        db = FirebaseDatabase.getInstance();
        dbref = db.getReference("drivers");
        agents = dbref.child(userName).child("trips").child(tripName).child("agents");
//        agentsNames.clear();
        agents.addValueEventListener(new ValueEventListener() {
            @SuppressLint("NotifyDataSetChanged")
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                Toast.makeText(getApplicationContext(), "You have " + snapshot.getChildrenCount() + " Agents in this trip .", Toast.LENGTH_SHORT).show();
                agentsNames.clear();
//                System.out.println("data from Firebase : "+snapshot.getValue());

                for (DataSnapshot dataSnapshot : snapshot.getChildren()) {
                    agent agent = dataSnapshot.getValue(agent.class);
                    agentsNames.add(agent);
//                        myAdapter = new AgentAdapter(agentsNames, getApplicationContext());
//                        recyclerView.setAdapter(myAdapter);
//                    System.out.println("data from Firebase : " + dataSnapshot.child("presence").getValue());


                }
                myAdapter.notifyDataSetChanged();

            }


            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                Toast.makeText(getApplicationContext(), "Loading Data Error : "+error, Toast.LENGTH_SHORT).show();
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

//    @Override
//    public void onBackPressed() {
//        super.onBackPressed();
//        startActivity(new Intent(this, TripsList.class));
//        finish();
//    }

    @Override
    protected void onPause() {
        super.onPause();
        Toast.makeText(getApplicationContext(), "Paused", Toast.LENGTH_SHORT).show();
    }
}