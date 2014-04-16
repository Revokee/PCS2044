package com.example.coopizza;

import java.util.ArrayList;

import Model.Entrega;
import Model.Pedido;
import android.net.Uri;
import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

public class ListActivity extends Activity {

	private final String TAG = "cooPizza";
	private ListView listPedidos; 
	private Entrega entrega;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
				
		
		// Restore any saved state 
		super.onCreate(savedInstanceState);
		setTitle("Lista de Pedidos");
		
		// Set content view
		setContentView(R.layout.activity_list);
		
//		// Get Entrega
//		entrega = (Entrega) getIntent().getSerializableExtra("Entrega.class");
//		
//		// Initialize UI elements
//		listPedidos = (ListView) findViewById(R.id.listView1);
//		
//		
//		//String[] list = new String[] { "Pedido 1","Pedido 2"};
//		
//		final ArrayList<String> list = new ArrayList<String>();
//	    for (int i = 0; i < entrega.listaPedidos.size(); ++i) {
//	      list.add(entrega.listaPedidos.get(i).getNomePedido()+" - "+entrega.listaPedidos.get(i).getNomeCliente());
//	    }
//		
//		ArrayAdapter<String> codeLearnArrayAdapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, list);
//				
//		listPedidos.setAdapter(codeLearnArrayAdapter);
//		// Link UI elements to actions in code	
//		
//		listPedidos.setOnItemClickListener(new AdapterView.OnItemClickListener() {
//
//		      @Override
//		      public void onItemClick(AdapterView<?> parent, final View view,
//		          int position, long id) {
//		        final String item = (String) parent.getItemAtPosition(position);
//		        
//		        Toast.makeText(getApplicationContext(),
//		        	      "Click ListItem Number " + position + "  Item " + item, Toast.LENGTH_LONG)
//		        	      .show();
//		        
//		      }
//
//		    });
//			
//		
	}
	
//	private void startPedidoActivity(Pedido pedido) {
//		try {
//			Intent pedidoIntent = new Intent(this, PedidoActivity.class);
//			startActivity(pedidoIntent);
//			pedidoIntent.putExtra("Pedido.class", pedido);
//		} catch (Exception e) {
//			Log.e(TAG, e.toString());
//		}
//	}

	

}
