package com.example.coopizza;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;

public class RouteActivity extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		
		// Restore any saved state 
		super.onCreate(savedInstanceState);
		// Set content view
		setContentView(R.layout.activity_route);
		
		
		
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.route, menu);
		return true;
	}

}
