import glob
import folium
from folium.plugins import MarkerCluster
import pandas as pd


def WindInBetrieb():

    print("Starting to resolve")
    path = r"source\\wea"

    all_files = glob.glob(path + "/*.csv")
    li = []
    for filename in all_files:
        df = pd.read_csv(filename,  on_bad_lines='skip', sep = ";", decimal= ".")
        li.append(df)

    dfAll = pd.concat(li, axis=0, ignore_index=True)

    m = folium.Map((51.24927460972442, 9.955969761190305), zoom_start= 6,tiles = 'cartodbpositron')
    marker_cluster = MarkerCluster().add_to(m)

    dfAll["Koordinate: Breitengrad (WGS84)"] = dfAll["Koordinate: Breitengrad (WGS84)"].str.replace(',','.', regex= True).astype(float)
    dfAll["Koordinate: Längengrad (WGS84)"] = dfAll["Koordinate: Längengrad (WGS84)"].str.replace(',','.', regex= True).astype(float)
    
    for index, each in dfAll.iterrows():
        
        try:

            iframe = folium.IFrame("<b> Name: " + str(each['Anzeige-Name der Einheit']) + "</b>" + '<br>' 
                                   + 'Bruttoleistung: ' + str(each['Bruttoleistung der Einheit']) + " kW" + '<br>' 
                                   + 'IBN Datum: ' + str(each['Inbetriebnahmedatum der Einheit']) + "<br>" 
                                   + 'Hersteller: ' + str(each['Hersteller der Windenergieanlage']) + "<br>" 
                                   + 'Typenbezeichnung: ' + str(each['Typenbezeichnung']) + "<br>" 
                                   + 'Spannungsebene: ' + str(each['Spannungsebene']))
            popup = folium.Popup(iframe, min_width=300, max_width=300)

            folium.Marker((each["Koordinate: Breitengrad (WGS84)"], each["Koordinate: Längengrad (WGS84)"]), popup = popup).add_to(marker_cluster)
        except Exception as e: pass

    folium.LayerControl().add_to(m)
    folium.plugins.LocateControl(auto_start=False).add_to(m)

    m.save("WEAinBetrieb.html")

    print("done")

WindInBetrieb()
