package com.saccomxd.baghdadi.yassine;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;

public class AgentsList extends AppCompatActivity {
    ArrayList<String> agentsNames;
    RecyclerView recyclerView;
    MyAdapter2 myAdapter;

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

        recyclerView = findViewById(R.id.myrec);
        recyclerView.setHasFixedSize(true);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        db = FirebaseDatabase.getInstance();
        dbref = db.getReference("drivers");
//        list = new ArrayList<agents>();
        agentsNames = new ArrayList<>();
        myAdapter = new MyAdapter2(this,agentsNames);
        recyclerView.setAdapter(myAdapter);
        pref = this.getSharedPreferences("var", Context.MODE_PRIVATE);
        editor = pref.edit();
        userName = pref.getString("user", null);
        tripName = pref.getString("trip", null);
        agents = dbref.child(userName).child("trips").child(tripName).child("agents");
        agents.addValueEventListener(new ValueEventListener() {
            @SuppressLint("NotifyDataSetChanged")
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                Toast.makeText(getApplicationContext(), "You have " + snapshot.getChildrenCount() + " Agents in this trip .", Toast.LENGTH_SHORT).show();
//
                for(DataSnapshot dataSnapshot : snapshot.getChildren()){
                    String agent = (String) dataSnapshot.getValue();
                    agentsNames.add(agent);
                    System.out.println(agentsNames);

                }
                myAdapter.notifyDataSetChanged();
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });



    }

}