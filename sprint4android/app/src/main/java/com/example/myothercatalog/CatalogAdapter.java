package com.example.myothercatalog;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class CatalogAdapter extends RecyclerView.Adapter<CatalogViewHolder> {

    private CatalogSkin catalogSkin;

    public CatalogAdapter(CatalogSkin catalogSkin) {
        this.catalogSkin = catalogSkin;
    }

    @NonNull
    @Override
    public CatalogViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        LayoutInflater layoutInflater = LayoutInflater.from(parent.getContext());

        View cellView = layoutInflater.inflate(R.layout.skin_recycler_view, parent, false);

        CatalogViewHolder catalogViewHolder = new CatalogViewHolder(cellView);

        return catalogViewHolder;
    }

    @Override
    public void onBindViewHolder(@NonNull CatalogViewHolder holder, int position) {
        Skin skin = this.catalogSkin.getSkinList().get(position);
        holder.showCatalog(skin);
    }

    @Override
    public int getItemCount() {
            return catalogSkin.getSkinList().size();
    }
}
