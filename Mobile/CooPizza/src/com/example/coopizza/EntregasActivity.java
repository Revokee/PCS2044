package com.example.coopizza;

import java.util.ArrayList;

import com.google.gson.Gson;

import Model.Entrega;
import Model.Pedido;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.SharedPreferences.Editor;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

public class EntregasActivity extends Activity {

	private final String TAG = "cooPizza";
	private ArrayList<Entrega> listaEntregas = new ArrayList<Entrega>();
	
	
	//Creating a shared preference
	
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
				

		
		// Restore any saved state 
		super.onCreate(savedInstanceState);
		setTitle("Lista de Entregas");
		
		// Set content view
		setContentView(R.layout.activity_entregas);
//		
//		// Initialize UI elements
//		listPedidos = (ListView) findViewById(R.id.listEntregas);
//		
//		String[] codeLearnChapters = new String[] { "Entrega 1","Entrega 2"};
//		
//		ArrayAdapter<String> codeLearnArrayAdapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, codeLearnChapters);
//				
//		listPedidos.setAdapter(codeLearnArrayAdapter);
//		// Link UI elements to actions in code	
//		

		buscarEntregas();
		final ListView listview = (ListView) findViewById(R.id.listEntregas);
		
//	    String[] values = new String[] { "Entrega 1", "Entrega 2", "Entrega 3",
//	        "Entrega 4", "Entrega 5", "Entrega 6"};

	    final ArrayList<String> list = new ArrayList<String>();
	    for (int i = 0; i < listaEntregas.size(); ++i) {
	      list.add(listaEntregas.get(i).getNome());
	    }
	    ArrayAdapter<String> adapter = new ArrayAdapter<String>(this,
	        android.R.layout.simple_list_item_1, list);
	    listview.setAdapter(adapter);

	    listview.setOnItemClickListener(new AdapterView.OnItemClickListener() {

	      @Override
	      public void onItemClick(AdapterView<?> parent, final View view,
	          int position, long id) {
	        final String item = (String) parent.getItemAtPosition(position);
	        
	        //sharedEntrega((Entrega)listaEntregas.get((int)position));
	        startMainActivity((Entrega)listaEntregas.get((int)position));
	        
	      }

	    });

		
		
	}


	//Start the MainActivity
	
	private void startMainActivity(Entrega entrega) {
		try {
			Intent mainIntent = new Intent(this, MainActivity.class);
			startActivity(mainIntent);
			//mainIntent.putExtra("Entrega.class", entrega); 
			
		} catch (Exception e) {
			Log.e(TAG, e.toString());
		}
	}
	
	
	//Pegar Lista de Entregas no Servidor
	
	private void buscarEntregas(){
		
		Log.e("Entregas", "buscar Entregas");
		Pedido pedido1 = new Pedido("Pedido 2", "Maria", "Rua Valson Lopes 70 ap 200", "Pizza Mussarela + Coca Cola", "R$35");
		Pedido pedido2 = new Pedido("Pedido 2", "Joao", "Rua Consolacao 100 ap 11", "Pizza 4 Queijos + Coca Cola", "R$35");
		Entrega entrega1 = new Entrega("Entrega 1");
		Entrega entrega2 = new Entrega("Entrega 2");
		
		entrega1.listaPedidos.add(pedido1);
		entrega1.listaPedidos.add(pedido2);
		entrega2.listaPedidos.add(pedido1);
		entrega2.listaPedidos.add(pedido2);

		
		listaEntregas.add(entrega1);
		listaEntregas.add(entrega2);
		
	}
	
	private void sharedEntrega(Entrega entrega)
	{	
		SharedPreferences  mPrefs = getPreferences(MODE_PRIVATE);
		Editor prefsEditor = mPrefs.edit();
	    Gson gson = new Gson();
	    String json = gson.toJson(entrega);
	    prefsEditor.putString("Entrega", json);
	    prefsEditor.commit();
	}

	
}
