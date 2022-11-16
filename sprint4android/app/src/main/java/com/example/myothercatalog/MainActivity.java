package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;

public class MainActivity extends AppCompatActivity {

    private CatalogSkin catalogSkin;
    private RecyclerView recyclerView;
    RequestQueue queue;

    public void setCatalogSkin(CatalogSkin catalogSkin) {
        this.catalogSkin = catalogSkin;

        CatalogAdapter catalogAdapter = new CatalogAdapter(catalogSkin);
        recyclerView.setAdapter(catalogAdapter);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        queue = Volley.newRequestQueue(this);

        recyclerView = findViewById(R.id.CatalogRecyclerView);



        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET,
                "https://raw.githubusercontent.com/llorchcluni/Desing-de-Interfaces/master/API-REST/catalog.json",
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        CatalogSkin serverparsedresponde = new CatalogSkin(response);
                        setCatalogSkin(serverparsedresponde);
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {

                    }
                }


        );
        this.queue.add(request);

    }
}