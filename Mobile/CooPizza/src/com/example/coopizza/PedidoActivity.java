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
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
				

		
		// Restore any saved state 
		super.onCreate(savedInstanceState);
		setTitle("Lista de Entregas");
		
		// Set content view
		setContentView(R.layout.activity_pedido);

		// Initialize UI elements
		final Button entregadaBtn = (Button) findViewById(R.id.buttonEntregada);
		final TextView txtEntrega = (TextView) findViewById(R.id.textViewEntrega);
		final TextView txtCliente = (TextView) findViewById(R.id.textViewCliente);
		final TextView txtEndereco = (TextView) findViewById(R.id.TextViewEndereco);
		final TextView txtProduto = (TextView) findViewById(R.id.TextViewProdutos);
		final TextView txtValora = (TextView) findViewById(R.id.TextViewValor);

	// Link UI elements to actions in code	
		entregadaBtn.setOnClickListener(new Button.OnClickListener() {			
			@Override
			public void onClick(View v) {				
				realizarEntrega();				
			}		
				
		});
			
	}

	
	void realizarEntrega()
	{
		
	}
	
	
}
