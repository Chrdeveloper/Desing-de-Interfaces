package com.example.myothercatalog;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.List;

public class CatalogSkin {

    List<Skin> skinList;


    public CatalogSkin(JSONArray jsonArray){
        for(int i = 0; i<jsonArray.length();i++){
            try {
                JSONObject jsonObject = jsonArray.getJSONObject(i);
                Skin character = new Skin(jsonObject);

                skinList.add(character);
            }catch (JSONException ex){
                throw new RuntimeException(ex);
            }
    }
}
    public List<Skin> getSkinList() {
        return skinList;
    }

    public void setSkinList(List<Skin> skinList) {
        this.skinList = skinList;
    }

}
