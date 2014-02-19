package com.example.coopizza;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.util.Log;
import android.view.View;
import android.widget.Button;

public class MainActivity extends Activity {

	private final String TAG = "cooPizza";
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
				
		
		// Restore any saved state 
		super.onCreate(savedInstanceState);
		
		// Set content view
		setContentView(R.layout.activity_list);
		
		// Initialize UI elements
		//final Button routeBtn = (Button) findViewById(R.id.buttonRoute);
		final Button listBtn = (Button) findViewById(R.id.buttonList);
		
		// Link UI elements to actions in code	
		listBtn.setOnClickListener(new Button.OnClickListener() {
			
			@Override
			public void onClick(View v) {				
				startListActivity();				
			}		
			
		});
		
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
	/*
	private void startRouteActivity() {
		try {
			
		} catch (Exception e) {
			Log.e(TAG, e.toString());
		}
	}
	*/
	
}
