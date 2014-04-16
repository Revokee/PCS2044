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

public class PedidoActivity extends Activity {

	private final String TAG = "cooPizza";
	private Pedido pedido;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
						
		// Restore any saved state 
		super.onCreate(savedInstanceState);
		setTitle("Lista de Entregas");
		
		// Set content view
		setContentView(R.layout.activity_pedido);

		
		pedido = gerarDummyPedido();
		
		// Initialize UI elements

		final Button routeBtn = (Button) findViewById(R.id.buttonRouteEntrega);
		final Button entregaRealizadaBtn = (Button) findViewById(R.id.buttonEntregaRealizada);
		final TextView txtEntrega = (TextView) findViewById(R.id.textViewEntrega);
		final TextView txtCliente = (TextView) findViewById(R.id.textViewCliente);
		final TextView txtEndereco = (TextView) findViewById(R.id.TextViewEndereco);
		final TextView txtProduto = (TextView) findViewById(R.id.TextViewProdutos);
		final TextView txtValor = (TextView) findViewById(R.id.TextViewValor);
		
		
		txtEntrega.setText(pedido.getNomePedido());
		txtCliente.setText(pedido.getNomeCliente());
		txtEndereco.setText(pedido.getEndereco());
		txtProduto.setText(pedido.getProdutos());
		txtValor.setText(pedido.getValor());
		

	 //Link UI elements to actions in code	
		routeBtn.setOnClickListener(new Button.OnClickListener() {			
			@Override
			public void onClick(View v) {				
				startRouteActivity();				
			}		
				
		});
		
		entregaRealizadaBtn.setOnClickListener(new Button.OnClickListener() {			
			@Override
			public void onClick(View v) {				
				startListActivity();				
			}		
				
		});
			
		
		
		
	}

	
	void realizarEntrega()
	{
		
	}
	
	private Pedido gerarDummyPedido(){
		
		Log.e("Entregas", "buscar Entregas");
		Pedido pedido1 = new Pedido("Pedido 1", "Maria", "Rua Valson Lopes 70 ap 200", "Pizza Mussarela + Coca Cola", "R$35");


		return pedido1;
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
	
	//Start the RouteActivity
	
		private void startListActivity() {
			try {
				Intent listIntent = new Intent(this, ListActivity.class);
				startActivity(listIntent);
				
			} catch (Exception e) {
				Log.e(TAG, e.toString());
			}
		}
	
	
}
