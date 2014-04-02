package com.example.coopizza;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.util.Log;

public class PushLocationService extends Service {
	
	public void onStartCommand() {
		Log.w("CooPizza", "YEAH! YEAH!");
		while(true) {
			try {
				Log.w("CooPizza", "Teste");
				Thread.sleep(500);
			} catch (InterruptedException e) {
				Log.e("CooPizza", "Service crashing...");
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
	
	public void onCreate() {
		Log.w("CooPizza", "YEAH!");
		this.onStartCommand();
	}

	@Override
	public IBinder onBind(Intent intent) {
		// TODO Auto-generated method stub
		return null;
	}
}
