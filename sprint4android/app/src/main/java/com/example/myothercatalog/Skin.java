package com.example.myothercatalog;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.renderscript.ScriptGroup;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;

public class Skin {
    private Bitmap imagenBitMap;
    private String nombre;

    public Skin(JSONObject jsonObject){
        try {
            String image = jsonObject.getString("image_url");
            URL url = new URL(image);
            URLConnection connection = url.openConnection();
            InputStream inputStream = connection.getInputStream();
            this.imagenBitMap = BitmapFactory.decodeStream(inputStream);

            this.nombre = jsonObject.getString("name");
        }catch (JSONException ex){
            throw new RuntimeException();
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
    public Bitmap getImage() {
        return imagenBitMap;
    }

    public String getNombre() {
        return nombre;
    }

}
