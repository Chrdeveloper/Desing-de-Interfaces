package com.example.myothercatalog;

import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class CatalogViewHolder extends RecyclerView.ViewHolder {

    private Skin skin;
    private TextView textView;
    private ImageView imageView;
    public CatalogViewHolder(@NonNull View itemView) {
        super(itemView);
        textView.findViewById(R.id.SkinText);
        imageView.findViewById(R.id.SkinImage);
    }

    public void showCatalog(Skin skin){
        this.skin = skin;
        String nombre = skin.getNombre();
        this.textView.setText(nombre);

        Util.downloadBitmapToImageView(skin.getImagen(), this.imageView);

    }

}
