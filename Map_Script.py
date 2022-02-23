import folium
import pandas as pd
from folium.plugins import *
from folium import *

m=folium.Map(location=[0.510440, 101.438309],zoom_start=12)
df=pd.read_csv("lokasi.csv")
all_group = FeatureGroup(name='All', show=False)
markercluster=MarkerCluster(control=False).add_to(m)

feature_group = FeatureGroupSubGroup(markercluster,"KFC")
feature_group2 = FeatureGroupSubGroup(markercluster,"Warung Steak")
feature_group3 = FeatureGroupSubGroup(markercluster,"Starbucks")
feature_group4 = FeatureGroupSubGroup(markercluster,"J.Co")
feature_group5 = FeatureGroupSubGroup(markercluster,"MCD")
feature_group6 = FeatureGroupSubGroup(markercluster,"Hoka-Hoka Bento")
feature_group7 = FeatureGroupSubGroup(markercluster,'AW')
feature_group5 = FeatureGroupSubGroup(markercluster,"MCD")
feature_group6 = FeatureGroupSubGroup(markercluster,"Hoka-Hoka Bento")
feature_group7 = FeatureGroupSubGroup(markercluster,"AW")
feature_group8 = FeatureGroupSubGroup(markercluster,"Pizza Hut")
feature_group9 = FeatureGroupSubGroup(markercluster,'CFC')
feature_group10 = FeatureGroupSubGroup(markercluster,"Burger King")
feature_group11 = FeatureGroupSubGroup(markercluster,"Solaria")

for i, row in df.iterrows():
    lat = df.at[i, "lat"]
    lon = df.at[i, 'lon']
    nama = df.at[i, "Nama"]
    deskripsi = df.at[i, "deskripsi"]

    if nama == 'KFC':
        warna = 'red'
        tengah = 'white'
        f= feature_group
        #icon3=folium.features.CustomIcon('KFC1.png',icon_size=(40, 60))
    elif nama == "Waroeng Steak":
        warna = "black"
        tengah = "beige"
        f= feature_group2
        #icon3 =folium.features.Customlcon("WS.png",icon_size=(40, 60))


    folium.Marker(location=[lat, lon], popup=nama,icon=folium.features.CustomIcon("kfc.png",icon_size=(30,30))).add_to(all_group)
    all_group.add_to(m)
    folium.Marker(location=[lat, lon], tooltip=nama,popup=deskripsi, icon=folium.Icon(color=warna,icon_color=tengah)).add_to(f)
    f.add_to(m)

LayerControl().add_to(m)
print(df.dtypes)
m.save("map.html")


