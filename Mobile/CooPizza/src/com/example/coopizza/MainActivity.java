package com.example.coopizza;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.widget.Button;

public class MainActivity extends Activity {

	private final String TAG = "cooPizza";
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
				
		
		// Restore any saved state 
		super.onCreate(savedInstanceState);
		
		// Set content view
		setContentView(R.layout.activity_main);
		
		// Initialize UI elements
		final Button listBtn = (Button) findViewById(R.id.buttonList);
		final Button routeBtn = (Button) findViewById(R.id.buttonRoute);
		
		// Link UI elements to actions in code	
		listBtn.setOnClickListener(new Button.OnClickListener() {			
			@Override
			public void onClick(View v) {				
				startListActivity();				
			}		
			
		});
		
		routeBtn.setOnClickListener(new Button.OnClickListener() {
			@Override
			public void onClick(View v) {
				startRouteActivity();
			}
		});
		
	}
	
	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}
	
	//Start the ListActivity
	
	private void startListActivity() {
		try {
			Intent listIntent = new Intent(this, ListActivity.class);
			startActivity(listIntent);
			
		} catch (Exception e) {
			Log.e(TAG, e.toString());
		}
	}
	
	//Start the RouteActivity
	
	private void startRouteActivity() {
		try {
			Intent routeIntent = new Intent(this, RouteActivity.class);
			startActivity(routeIntent);
			
		} catch (Exception e) {
			Log.e(TAG, e.toString());
		}
	}
	
	
}
