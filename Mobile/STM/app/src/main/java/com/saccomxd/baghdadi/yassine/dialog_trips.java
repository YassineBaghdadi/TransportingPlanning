package com.saccomxd.baghdadi.yassine;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.app.Dialog;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.time.temporal.TemporalAccessor;

public class dialog_trips {
    FirebaseDatabase fDb;
    DatabaseReference db;
    private String type;
    boolean started, finiched;
    int startedCounterKM;

    public void showdialog(Context activity) {
        final Dialog dialog = new Dialog(activity, R.style.DialogAnimation);
        dialog.requestWindowFeature(Window.FEATURE_NO_TITLE);
        dialog.setCancelable(true);
        dialog.setContentView(R.layout.custom_dialog);
//        dialog.setCanceledOnTouchOutside(true);
        SharedPreferences sharedPreferences = activity.getSharedPreferences("var", Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPreferences.edit();
        TextView action = (TextView) dialog.findViewById(R.id.action);
        EditText counter = (EditText) dialog.findViewById(R.id.counter);

        TextView viewbtn = (TextView) dialog.findViewById(R.id.view);
        fDb = FirebaseDatabase.getInstance();
        db = fDb.getReference("drivers").child(sharedPreferences.getString("user", null)).child("trips").child(sharedPreferences.getString("trip", null));
        db.addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {

                if (snapshot.hasChild("startcounter") && snapshot.hasChild("stopcounter")) {
                    action.setText("Finiched");
                    action.setBackgroundResource(R.drawable.rouded_corner_gray);
                    started = true;
                    finiched = true;
                    action.setEnabled(false);
                    counter.setEnabled(false);
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

                    if (started) {
                        if (Integer.parseInt(counter.getText().toString()) > startedCounterKM){
                            db.child("stopcounter").setValue(counter.getText().toString());
                            activity.startActivity(new Intent(activity, AgentsList.class));
                            dialog.dismiss();
                        }else {
                            Toast.makeText(activity, "The Stop Counter has to be Greater than The Start one ", Toast.LENGTH_SHORT).show();
                        }
                    } else {
                        db.child("startcounter").setValue(counter.getText().toString());
                        activity.startActivity(new Intent(activity, AgentsList.class));
                        dialog.dismiss();
                    }

                }


            }
        });


        dialog.show();

    }
}