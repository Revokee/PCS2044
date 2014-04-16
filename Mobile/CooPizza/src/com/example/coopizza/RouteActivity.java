package com.example.coopizza;

import com.google.android.gms.maps.CameraUpdate;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.MapFragment;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;
import android.R.string;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Bitmap;
import android.location.Location;
import android.location.LocationListener;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentActivity;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

public class RouteActivity extends FragmentActivity implements LocationListener {
	
	private GoogleMap googlemap;
	int iniciar = 0;

	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		
		// Restore any saved state 
		LatLng LOCATION_ATUAL = new LatLng(-23.568560, -46.743762);
		super.onCreate(savedInstanceState);
		// Set content view
		setContentView(R.layout.activity_route);
		
		
		InitMap();
		addMarkerToMap(-23.568560, -46.743762, "Maria", "Rua Valson Lopes");
		 
	    CameraUpdate update = CameraUpdateFactory.newLatLngZoom(LOCATION_ATUAL, 16);
	    googlemap.animateCamera(update);
		//addMarkerToMap(38.0000000, -125.0000000, "Eduardo", "Whatever");
	}
	
	
	private void addMarkerToMap(double latitude, double longitude, String nome, String endereco) {
		LatLng pos = new LatLng(latitude, longitude);
		
		googlemap.addMarker(new MarkerOptions()
				.title(nome)
				.snippet(endereco)
				.icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_BLUE))
				.position(pos)
				);
				
		
	}
	
//	public View onCreateView(LayoutInflater inflater, ViewGroup container,
//            Bundle savedInstanceState) {
//            // Inflate the layout for this fragment
//            return inflater.inflate(R.layout.activity_route, container, false);
//	}

	@Override
	public void onLocationChanged(Location location) {
	
	}

	@Override
	public void onProviderDisabled(String provider) {

	}

	@Override
	public void onProviderEnabled(String provider) {
		AlertDialog.Builder builder = new AlertDialog.Builder(this);
		builder.setTitle("GPS is Enabled");
		builder.setCancelable(false);
		builder.setPositiveButton("Enabled GPS", new DialogInterface.OnClickListener() {
			
			public void onClick(DialogInterface dialog, int which) {
				Intent startGps = new Intent(android.provider.Settings.ACTION_LOCATION_SOURCE_SETTINGS);
				startActivity(startGps);
			}
		});
		builder.setNegativeButton("Leave GPS off", new DialogInterface.OnClickListener() {
			
			public void onClick(DialogInterface dialog, int which) {
				dialog.cancel();
				
			}
		});
		AlertDialog alert = builder.create();
		alert.show();
		
		
	}

	@Override
	public void onStatusChanged(String provider, int status, Bundle extras) {
	
	}
	
	private void InitMap(){
		SupportMapFragment mf = (SupportMapFragment) getSupportFragmentManager().findFragmentById(R.id.map);
		googlemap = mf.getMap();
		
		googlemap.setMyLocationEnabled(true);
		googlemap.setMapType(GoogleMap.MAP_TYPE_NORMAL);
	}
	

//	@Override
//	public boolean onCreateOptionsMenu(Menu menu) {
//		// Inflate the menu; this adds items to the action bar if it is present.
//		getMenuInflater().inflate(R.menu.route, menu);
//		return true;
//	}

}