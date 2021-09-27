package com.saccomxd.baghdadi.yassine;

import android.Manifest;
import android.content.Context;
import android.content.pm.PackageManager;
import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.location.LocationManager;
import android.widget.Toast;

import androidx.core.app.ActivityCompat;

import java.util.List;
import java.util.Locale;

public class variables {
    public String user ;

    private Location gps_loc;
    Location network_loc;
    Location final_loc;
    double longitude;
    double latitude;
    String userCountry, userAddress;


    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
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
//                Toast.makeText(context, "Latitude : "+addresses.get(0).getLatitude()+" - Longitude : "+addresses.get(0).getLongitude(), Toast.LENGTH_SHORT).show();
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
}
