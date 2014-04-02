package com.example.coopizza;
//
//import android.app.Activity;
//import android.os.Bundle;
//import android.view.Menu;
//
//import com.google.android.gms.maps.CameraUpdateFactory;
//import com.google.android.gms.maps.GoogleMap;
//import com.google.android.gms.maps.MapFragment;
//import com.google.android.gms.maps.model.BitmapDescriptorFactory;
//import com.google.android.gms.maps.model.LatLng;
//import com.google.android.gms.maps.model.Marker;
//import com.google.android.gms.maps.model.MarkerOptions;
//import android.os.Bundle;
//import android.support.v4.app.Fragment;
//import android.view.LayoutInflater;
//import android.view.View;
//import android.view.ViewGroup;
//
//public class RouteActivity extends Activity {
//	static final LatLng HAMBURG = new LatLng(53.558, 9.927);
//	static final LatLng KIEL = new LatLng(53.551, 9.993);
//	private GoogleMap map;
//	
//	@Override
//	protected void onCreate(Bundle savedInstanceState) {
//	    super.onCreate(savedInstanceState);
//	    setContentView(R.layout.activity_main);
//	    map = ((MapFragment) getFragmentManager().findFragmentById(R.id.map))
//	        .getMap();
//	    Marker hamburg = map.addMarker(new MarkerOptions().position(HAMBURG)
//	        .title("Hamburg"));
//	    Marker kiel = map.addMarker(new MarkerOptions()
//		    .position(KIEL)
//		    .title("Kiel")
//		    .snippet("Kiel is cool")
//		    .icon(BitmapDescriptorFactory
//		    .fromResource(R.drawable.ic_launcher)));
//	  }
//	
//}


import android.app.Activity;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.View;
import android.view.ViewGroup;

public class RouteActivity extends Activity {
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		
		// Restore any saved state 
		super.onCreate(savedInstanceState);
		// Set content view
		setContentView(R.layout.activity_route);
	}
	
	public View onCreateView(LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState) {
            // Inflate the layout for this fragment
            return inflater.inflate(R.layout.activity_route, container, false);
    }

//	@Override
//	public boolean onCreateOptionsMenu(Menu menu) {
//		// Inflate the menu; this adds items to the action bar if it is present.
//		getMenuInflater().inflate(R.menu.route, menu);
//		return true;
//	}

}
