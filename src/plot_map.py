import folium
import pandas as pd
import glob

data_path_list = glob.glob('/Users/ogurayuudai/Desktop/personal-dev/map-application/data/processed_data/*')[:2]

map = folium.Map(location=[36.288055, 138.097424], zoom_start=10)
for data_path in data_path_list:
    df = pd.read_csv(data_path)
    for i, r in df.iterrows():
        if r.isnull().any():
            continue
        else:
            if r['point'] >= 95:
                folium.Marker(location=[r['latitude'], r['longitude']], popup=r['name']+':'+str(r['point'])+'pt.', icon=folium.Icon(color="red")).add_to(map)
            elif r['point'] >= 90:
                folium.Marker(location=[r['latitude'], r['longitude']], popup=r['name']+':'+str(r['point'])+'pt.', icon=folium.Icon(color="orange")).add_to(map)
            elif r['point'] >= 80:
                folium.Marker(location=[r['latitude'], r['longitude']], popup=r['name']+':'+str(r['point'])+'pt.', icon=folium.Icon(color="green")).add_to(map)
            else:
                folium.Marker(location=[r['latitude'], r['longitude']], popup=r['name']+':'+str(r['point'])+'pt.', icon=folium.Icon(color="lightgreen")).add_to(map)


map.save("ramen_map.html")