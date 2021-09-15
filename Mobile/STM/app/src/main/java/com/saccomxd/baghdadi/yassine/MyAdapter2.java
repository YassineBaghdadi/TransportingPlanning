package com.saccomxd.baghdadi.yassine;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.SharedPreferences;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.FrameLayout;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.chauthai.swipereveallayout.SwipeRevealLayout;
import com.chauthai.swipereveallayout.ViewBinderHelper;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Date;

public class MyAdapter2 extends RecyclerView.Adapter<MyAdapter2.MyViewHolder> {
    static boolean picked = false;
    Context context;

    ArrayList<String> list;
    private final ViewBinderHelper viewBinderHelper = new ViewBinderHelper();

    public MyAdapter2(Context context, ArrayList<String> list) {
        this.context = context;
        this.list = list;
    }


    @NonNull
    @Override
    public MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(context).inflate(R.layout.agent,parent,false);
        return  new MyViewHolder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull MyViewHolder holder, int position) {

        String trip = list.get(position);
        holder.agentName.setText(list.get(position));
        viewBinderHelper.setOpenOnlyOne(true);
        viewBinderHelper.bind(holder.swipRevealLayout,String.valueOf(list.get(position)));
        viewBinderHelper.closeLayout(String.valueOf(list.get(position)));


    }

    @Override
    public int getItemCount() {
        return list.size();
    }

    public static class MyViewHolder extends RecyclerView.ViewHolder{
        FirebaseDatabase database;
        DatabaseReference myRef;
        TextView agentName;
        ImageView enter, leave, abssent;
        SwipeRevealLayout swipRevealLayout;
        RelativeLayout rr;
        SharedPreferences pref;
        SharedPreferences.Editor editor;


        public MyViewHolder(@NonNull View itemView) {
            super(itemView);
            database = FirebaseDatabase.getInstance();
            myRef = database.getReference("drivers");
            pref = itemView.getContext().getSharedPreferences("var", Context.MODE_PRIVATE);
            editor = pref.edit();
            agentName = itemView.findViewById(R.id.agentName);
            swipRevealLayout = itemView.findViewById(R.id.swipRevealLayout);
            rr = itemView.findViewById(R.id.container);
            String currentTrip = pref.getString("trip", null);
            String user = pref.getString("user", null);
            enter = itemView.findViewById(R.id.enter);
            leave = itemView.findViewById(R.id.leave);
            abssent = itemView.findViewById(R.id.absent);

            rr.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    if (swipRevealLayout.isOpened()){
                        swipRevealLayout.close(true);
                    }else if (swipRevealLayout.isClosed()){
                        swipRevealLayout.open(true);
                    }
                }
            });


            enter.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    @SuppressLint("SimpleDateFormat") SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
                    Date date = new Date();
                    String datetime = formatter.format(date);
                    Toast.makeText(itemView.getContext(), agentName.getText() + " Entered The Van at : " + datetime.split("\\s+")[1], Toast.LENGTH_SHORT).show();
                    String time = datetime.split("\\s+")[0];
                    myRef.child(user).child("trips").child(currentTrip).child("picktime").child(agentName.getText().toString().split("\\s+")[0]).setValue(datetime.split("\\s+")[1]);
                    myRef.child(user).child("trips").child(currentTrip).child("presence").child(agentName.getText().toString().split("\\s+")[0]).setValue(1);

                    swipRevealLayout.close(true);


                }
            });
            leave.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    @SuppressLint("SimpleDateFormat") SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
                    Date date = new Date();
                    String datetime = formatter.format(date);

                    myRef.child(user).child("trips").child(currentTrip).child("droptime").child(agentName.getText().toString().split("\\s+")[0]).setValue(datetime.split("\\s+")[1]);
                    myRef.child(user).child("trips").child(currentTrip).child("presence").child(agentName.getText().toString().split("\\s+")[0]).setValue(1);
                    Toast.makeText(itemView.getContext(), "Leave BTN clicked", Toast.LENGTH_SHORT).show();
                    swipRevealLayout.close(true);
                }
            });
            abssent.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {

                    myRef.child(user).child("trips").child(currentTrip).child("picktime").child(agentName.getText().toString().split("\\s+")[0]).setValue(0);
                    myRef.child(user).child("trips").child(currentTrip).child("droptime").child(agentName.getText().toString().split("\\s+")[0]).setValue(0);
                    myRef.child(user).child("trips").child(currentTrip).child("presence").child(agentName.getText().toString().split("\\s+")[0]).setValue(0);
                    Toast.makeText(itemView.getContext(), "Abssent BTN clicked", Toast.LENGTH_SHORT).show();
                    swipRevealLayout.close(true);
                }
            });

        }
    }

}