package com.example.coopizza;

import java.util.ArrayList;

import android.net.Uri;
import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;

public class ListActivity extends Activity {

	private final String TAG = "cooPizza";
	private ListView listPedidos; 
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
				
		
		// Restore any saved state 
		super.onCreate(savedInstanceState);
		
		// Set content view
		setContentView(R.layout.activity_list);
		
		// Initialize UI elements
		listPedidos = (ListView) findViewById(R.id.listView1);
		
		String[] codeLearnChapters = new String[] { "Pedido 1","Pedido 2"};
		
		ArrayAdapter<String> codeLearnArrayAdapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, codeLearnChapters);
				
		listPedidos.setAdapter(codeLearnArrayAdapter);
		// Link UI elements to actions in code	
		
			
		
		
		
	}

	

}
