package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class Skin {
    private String imagen;
    private String nombre;
    private String descripcion;



    public Skin(JSONObject jsonObject) {
        try {
            imagen = jsonObject.getString("image_url");
            this.imagen = imagen;
            this.descripcion = jsonObject.getString("description");
            this.nombre = jsonObject.getString("name");
        } catch (JSONException ex) {
            throw new RuntimeException();

        }
    }
    public String getImagen() {
        return imagen;
    }

    public void setImagen(String imagen) {
        this.imagen = imagen;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }
}
