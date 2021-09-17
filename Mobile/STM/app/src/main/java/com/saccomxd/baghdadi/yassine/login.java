package com.saccomxd.baghdadi.yassine;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.Manifest;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;


import java.util.ConcurrentModificationException;
import java.util.Objects;

public class login extends AppCompatActivity {
    SharedPreferences pref;
    SharedPreferences.Editor editor;
    public EditText userName, passwrd;
    FirebaseDatabase db;
    DatabaseReference dbref;
    boolean connected;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        userName = (EditText) findViewById(R.id.username);
        passwrd = (EditText) findViewById(R.id.password);
        db = FirebaseDatabase.getInstance();
        dbref = db.getReference("drivers");
        ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION, Manifest.permission.ACCESS_NETWORK_STATE, Manifest.permission.CALL_PHONE}, 1);
        ConnectivityManager cm = (ConnectivityManager) getApplicationContext().getSystemService(Context.CONNECTIVITY_SERVICE);
        NetworkInfo nInfo = cm.getActiveNetworkInfo();
        connected = nInfo != null && nInfo.isAvailable() && nInfo.isConnected();

        pref = getApplicationContext().getSharedPreferences("var", Context.MODE_PRIVATE);
        editor = pref.edit();


    }

    public void login(View view) {
        if (!connected) {
            ConnectivityManager cm = (ConnectivityManager) getApplicationContext().getSystemService(Context.CONNECTIVITY_SERVICE);
            NetworkInfo nInfo = cm.getActiveNetworkInfo();
            connected = nInfo != null && nInfo.isAvailable() && nInfo.isConnected();
            AlertDialog.Builder dlgAlert = new AlertDialog.Builder(this);
            dlgAlert.setMessage("No Internet Connection ...");
            dlgAlert.setTitle("STM : Connection Error");
            dlgAlert.setPositiveButton("OK", null);
            dlgAlert.setCancelable(false);
            dlgAlert.create().show();
        } else {
            dbref.addValueEventListener(new ValueEventListener() {
                @Override
                public void onDataChange(@NonNull DataSnapshot snapshot) {
                    //Toast.makeText(getApplicationContext(), snapshot.child(userName.getText().toString()).child("pass").getValue().toString(), Toast.LENGTH_SHORT).show();
                    if (snapshot.hasChild(userName.getText().toString())) {
                        if (Objects.equals(snapshot.child(userName.getText().toString()).child("pass").getValue(), passwrd.getText().toString())) {
                            editor.putString("user", userName.getText().toString());
                            editor.apply();

                            Intent intent = new Intent(login.this, TripsList.class);
//                        Bundle user = new Bundle();
//                        user.putString("user", userName.getText().toString());
//                        intent.putExtras(user);
                            startActivity(intent);
                        } else {
                            Toast.makeText(getApplicationContext(), "The Password Not Correct ...", Toast.LENGTH_SHORT).show();
                        }
                    } else {
                        Toast.makeText(getApplicationContext(), "No User Found ...", Toast.LENGTH_SHORT).show();
                    }
                }

                @Override
                public void onCancelled(@NonNull DatabaseError error) {

                }
            });
        }
    }
}