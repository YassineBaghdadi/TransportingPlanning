package com.saccomxd.baghdadi.yassine;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Handler;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.cardview.widget.CardView;
import androidx.recyclerview.widget.RecyclerView;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.Objects;

public class MyAdapter extends RecyclerView.Adapter<MyAdapter.MyViewHolder> {
    SharedPreferences pref;
    SharedPreferences.Editor editor;
    private Context context;
    private Activity activity;
    CardView mycard;
    ArrayList<String> list;
    private MyViewHolder holder;
    private int position;
    private String active_trip;

    Handler handler = new Handler();
    Runnable runnable;
    int delay = 1000;

    public MyAdapter(Context context, ArrayList<String> list) {
        this.context = context;
        this.list = list;
        setHasStableIds(true);
    }


    @NonNull
    @Override
    public MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(context).inflate(R.layout.trip, parent, false);

        return new MyViewHolder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull MyViewHolder holder, int position) {


        String trip = list.get(position);
        holder.tripName.setText(list.get(position));


    }

    @Override
    public int getItemCount() {
        return list.size();
    }

    public class MyViewHolder extends RecyclerView.ViewHolder {

        TextView tripName;
        Activity activity;

        public MyViewHolder(@NonNull View itemView) {
            super(itemView);
            context = itemView.getContext();
            tripName = itemView.findViewById(R.id.txt);
            mycard = itemView.findViewById(R.id.mycard);
            pref = itemView.getContext().getSharedPreferences("var", Context.MODE_PRIVATE);
            editor = pref.edit();

            active_trip = "0";
            FirebaseDatabase Fdb = FirebaseDatabase.getInstance();
            DatabaseReference db = Fdb.getReference("drivers").child(pref.getString("user", null)).child("trips");
            Fdb.getReference("drivers").child(pref.getString("user", null)).addListenerForSingleValueEvent(new ValueEventListener() {
                @Override
                public void onDataChange(@NonNull DataSnapshot snapshot) {
                    if (snapshot.hasChild("activetrip")) {
                        active_trip = String.valueOf(snapshot.child("activetrip").getValue());
                    }
                }

                @Override
                public void onCancelled(@NonNull DatabaseError error) {

                }
            });



            mycard.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    System.out.println("active trip ==> "+ active_trip);
                    if (active_trip.equals("0") || active_trip.equals(tripName.getText().toString())) {
                        editor.putString("trip", tripName.getText().toString());
                        editor.apply();
//                    Intent intent = new Intent(context, AgentsList.class);
//                    view.getContext().startActivity(intent);
                        String t;

                        dialog_trips d = new dialog_trips();
                        d.showdialog(context);
                    }

                }
            });

        }
    }

}