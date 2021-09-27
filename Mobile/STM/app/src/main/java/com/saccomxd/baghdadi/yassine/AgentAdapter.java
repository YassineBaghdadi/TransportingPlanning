package com.saccomxd.baghdadi.yassine;

import static android.content.Context.LOCATION_SERVICE;
import static androidx.core.content.ContextCompat.startActivity;

import android.Manifest;
import android.annotation.SuppressLint;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.graphics.Color;
import android.graphics.drawable.Drawable;
import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.location.LocationRequest;
import android.net.Uri;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.cardview.widget.CardView;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.chauthai.swipereveallayout.SwipeRevealLayout;
import com.chauthai.swipereveallayout.ViewBinderHelper;
import com.firebase.ui.database.FirebaseRecyclerAdapter;
import com.firebase.ui.database.FirebaseRecyclerOptions;
import com.google.android.gms.location.FusedLocationProviderClient;
import com.google.android.gms.location.LocationCallback;
import com.google.android.gms.location.LocationSettingsRequest;
import com.google.android.gms.location.SettingsClient;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.squareup.picasso.Picasso;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Locale;

public class AgentAdapter extends RecyclerView.Adapter<AgentAdapter.ViewHolder> {
    private ArrayList<agent> dataModalArrayList;
    private Context context;
    private final ViewBinderHelper viewBinderHelper = new ViewBinderHelper();
    static agent modal;



    private LocationManager locationManager;
    private LocationListener listener;

    // location last updated time
    private String mLastUpdateTime;
    private static String active_trip;

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

    public AgentAdapter(ArrayList<agent> dataModalArrayList, Context context) {
        this.dataModalArrayList = dataModalArrayList;
        this.context = context;
    }


    @NonNull
    @Override
    public AgentAdapter.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        return new ViewHolder(LayoutInflater.from(context).inflate(R.layout.agent, parent, false));
    }

    @Override
    public void onBindViewHolder(@NonNull AgentAdapter.ViewHolder holder, @SuppressLint("RecyclerView") int position) {

// setting data to our views in Recycler view items.
        modal = dataModalArrayList.get(position);


        holder.agentName.setText(modal.getName());
        holder.agentPhone.setText(modal.getPhone());
        holder.agentGrp.setText(modal.getGrp());
//        Picasso.get().load(modal.getPic()).into(holder.agentPic);
        Glide.with(context)
                .load(modal.getPic())
                .placeholder(R.drawable.load)
                .error(R.drawable.err)
                .into(holder.agentPic);
        viewBinderHelper.setOpenOnlyOne(true);
        viewBinderHelper.bind(holder.swipRevealLayout,String.valueOf(modal.getName()));
        viewBinderHelper.closeLayout(String.valueOf(modal.getName()));




        holder.abssent.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                holder.myRef.child(holder.user).child("trips").child(holder.currentTrip).child("agents").child(String.valueOf(position)).child("picktime").setValue(0);
                holder.myRef.child(holder.user).child("trips").child(holder.currentTrip).child("agents").child(String.valueOf(position)).child("droptime").setValue(0);
                holder.myRef.child(holder.user).child("trips").child(holder.currentTrip).child("agents").child(String.valueOf(position)).child("presence").setValue(0);
//                    Toast.makeText(itemView.getContext(), "Abssent BTN clicked", Toast.LENGTH_SHORT).show();
                holder.swipRevealLayout.close(true);
                holder.itemView.getContext().startActivity(new Intent(holder.itemView.getContext(), AgentsList.class));

            }
        });

        holder.enter.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                @SuppressLint("SimpleDateFormat") SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
                Date date = new Date();
                String datetime = formatter.format(date);
                Toast.makeText(holder.itemView.getContext(), holder.agentName.getText() + " Entered The Van at : " + datetime.split("\\s+")[1], Toast.LENGTH_SHORT).show();
                String time = datetime.split("\\s+")[0];
                holder.myRef.child(holder.user).child("trips").child(holder.currentTrip).child("agents").child(String.valueOf(position)).child("picktime").setValue(datetime.split("\\s+")[1]);
                holder.myRef.child(holder.user).child("trips").child(holder.currentTrip).child("agents").child(String.valueOf(position)).child("presence").setValue("1");
                holder.myRef.child(holder.user).child("trips").child(holder.currentTrip).child("agents").child(String.valueOf(position)).child("pickloc").setValue(getLocation(holder.itemView.getContext()));

                holder.swipRevealLayout.close(true);
                holder.itemView.getContext().startActivity(new Intent(holder.itemView.getContext(), AgentsList.class));


            }
        });
        holder.leave.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                @SuppressLint("SimpleDateFormat") SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
                Date date = new Date();
                String datetime = formatter.format(date);

                holder.myRef.child(holder.user).child("trips").child(holder.currentTrip).child("agents").child(String.valueOf(position)).child("droptime").setValue(datetime.split("\\s+")[1]);
                holder.myRef.child(holder.user).child("trips").child(holder.currentTrip).child("agents").child(String.valueOf(position)).child("presence").setValue("1");
                holder.myRef.child(holder.user).child("trips").child(holder.currentTrip).child("agents").child(String.valueOf(position)).child("droploc").setValue(getLocation(holder.itemView.getContext()));
                Toast.makeText(holder.itemView.getContext(), "Leave BTN clicked", Toast.LENGTH_SHORT).show();
                holder.swipRevealLayout.close(true);
                holder.itemView.getContext().startActivity(new Intent(holder.itemView.getContext(), AgentsList.class));
            }
        });

        holder.call.setOnClickListener(new View.OnClickListener() {


            @Override
            public void onClick(View view) {
//                System.out.println();
                Toast.makeText(context, "Calling : " + modal.getPhone(), Toast.LENGTH_SHORT).show();


                if (ActivityCompat.checkSelfPermission(context,
                        Manifest.permission.CALL_PHONE) != PackageManager.PERMISSION_GRANTED) {
                    return;
                }
                Intent intent = new Intent(Intent.ACTION_DIAL);
                intent.setData(Uri.parse("tel:"+modal.getPhone()));
                startActivity(context, intent, null);
            }

////                Intent intent = new Intent(Intent.ACTION_DIAL);
//                Intent intent = new Intent(Intent.ACTION_CALL);
//                intent.setData(Uri.parse("tel:"+modal.getPhone()));
//                context.startActivity(intent);



        });



    }


    public String getLocation(Context context){

        LocationManager locationManager = (LocationManager) context.getSystemService(Context.LOCATION_SERVICE);

        if (ActivityCompat.checkSelfPermission(context, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED
                && ActivityCompat.checkSelfPermission(context, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED
                && ActivityCompat.checkSelfPermission(context, Manifest.permission.ACCESS_NETWORK_STATE) != PackageManager.PERMISSION_GRANTED) {

            return "error";
        }

        try {

            gps_loc = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);
            network_loc = locationManager.getLastKnownLocation(LocationManager.NETWORK_PROVIDER);

        } catch (Exception e) {
            e.printStackTrace();
        }
        if (gps_loc != null) {
            final_loc = gps_loc;
            latitude = final_loc.getLatitude();
            longitude = final_loc.getLongitude();
        }
        else if (network_loc != null) {
            final_loc = network_loc;
            latitude = final_loc.getLatitude();
            longitude = final_loc.getLongitude();
        }
        else {
            latitude = 0.0;
            longitude = 0.0;
        }
//        ActivityCompat.requestPermissions(this, new String[] {Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION, Manifest.permission.ACCESS_NETWORK_STATE}, 1);
        try {

            Geocoder geocoder = new Geocoder(context, Locale.getDefault());
            List<Address> addresses = geocoder.getFromLocation(latitude, longitude, 1);
            if (addresses != null && addresses.size() > 0) {
                userCountry = addresses.get(0).getCountryName();
                userAddress = addresses.get(0).getAddressLine(0);
                Toast.makeText(context, "Latitude : "+addresses.get(0).getLatitude()+" - Longitude : "+addresses.get(0).getLongitude(), Toast.LENGTH_SHORT).show();
//                editor.putString("loc", addresses.get(0).getLatitude()+","+addresses.get(0).getLongitude());
                return addresses.get(0).getLatitude()+","+addresses.get(0).getLongitude();


            }
            else {
                userCountry = "Unknown";

            }

        } catch (Exception e) {
            e.printStackTrace();
        }
        return "0";
    }


    @Override
    public int getItemCount() {
        return dataModalArrayList.size();
    }

    public static class ViewHolder extends RecyclerView.ViewHolder{
        private final TextView agentName;
        private final TextView agentPhone;
        private final TextView agentGrp;
        private final ImageView agentPic;
        private final FirebaseDatabase database;
        private final DatabaseReference myRef;
        private final SharedPreferences pref;
        private final SharedPreferences.Editor editor;
        private final SwipeRevealLayout swipRevealLayout;
        private final RelativeLayout rr;
        private final ImageView enter, leave, abssent, call;
        String user, currentTrip, tripName;


        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            agentName = itemView.findViewById(R.id.agentName);
            agentPhone = itemView.findViewById(R.id.phone);
            agentGrp = itemView.findViewById(R.id.agrntGrp);
            agentPic = itemView.findViewById(R.id.agent_pic);
            database = FirebaseDatabase.getInstance();
            myRef = database.getReference("drivers");
            pref = itemView.getContext().getSharedPreferences("var", Context.MODE_PRIVATE);
            editor = pref.edit();

            swipRevealLayout = itemView.findViewById(R.id.swipRevealLayout);
            rr = itemView.findViewById(R.id.agentcontainer);
            currentTrip = pref.getString("trip", null);
            user = pref.getString("user", null);
            enter = itemView.findViewById(R.id.enter);
            leave = itemView.findViewById(R.id.leave);
            abssent = itemView.findViewById(R.id.absent);
            call = itemView.findViewById(R.id.call);


            myRef.addListenerForSingleValueEvent(new ValueEventListener() {
                @Override
                public void onDataChange(@NonNull DataSnapshot snapshot) {
//                    System.out.println("Debagging "+ );
                    if (snapshot.child(user).hasChild("activetrip") && !String.valueOf(snapshot.child(user).child("activetrip").getValue()).equals(currentTrip)){
//                        swipRevealLayout.setLockDrag(true);
//                        rr.setEnabled(false);
                        enter.setEnabled(false);
                        leave.setEnabled(false);
                        abssent.setEnabled(false);
                        enter.setBackgroundResource(R.drawable.rouded_corner_gray);
                        leave.setBackgroundResource(R.drawable.rouded_corner_gray);
                        abssent.setBackgroundResource(R.drawable.rouded_corner_gray);
                    }
                }

                @Override
                public void onCancelled(@NonNull DatabaseError error) {

                }
            });

            System.out.println(active_trip+" And "+currentTrip);
//            if (!active_trip.equals(currentTrip)){
//                swipRevealLayout.setLockDrag(true);
//            }
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





        }
    }
}
