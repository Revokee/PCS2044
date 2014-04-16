package com.example.coopizza;

import java.io.ByteArrayOutputStream;
import java.io.IOException;

import org.apache.http.HttpResponse;
import org.apache.http.HttpStatus;
import org.apache.http.StatusLine;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.json.JSONException;
import org.json.JSONObject;

import android.os.AsyncTask;

public class NetworkTask extends AsyncTask<String, Void, JSONObject> {
	@Override
	protected JSONObject doInBackground(String... uri) {
		HttpClient httpclient = new DefaultHttpClient();
		HttpResponse httpresponse;
		JSONObject response = null;
		try {
			httpresponse = httpclient.execute(new HttpGet(uri[0]));
			StatusLine statusLine = httpresponse.getStatusLine();
			if(statusLine.getStatusCode() == HttpStatus.SC_OK){
				ByteArrayOutputStream out = new ByteArrayOutputStream();
				httpresponse.getEntity().writeTo(out);
				out.close();
				response = new JSONObject(out.toString());
			} else{
				//Closes the connection.
				httpresponse.getEntity().getContent().close();
				throw new IOException(statusLine.getReasonPhrase());
			}
		} catch (ClientProtocolException e) {
			//TODO Handle problems..
		} catch (IOException e) {
			//TODO Handle problems..
		} catch (JSONException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return response;
	}

	@Override
	protected void onPostExecute(JSONObject result) {
		super.onPostExecute(result);
		//Do anything with response..
	}
}
