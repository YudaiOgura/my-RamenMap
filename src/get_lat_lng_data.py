from geopy.geocoders import Nominatim
import pandas as pd
import googlemaps
import glob

ramen_data_path_list = [
    '/Users/ogurayuudai/Desktop/personal-dev/map-application/data/original_data/ramen_data51to100.csv',
    '/Users/ogurayuudai/Desktop/personal-dev/map-application/data/original_data/ramen_data101to150.csv'
]
output_data_path_list = [
    '/Users/ogurayuudai/Desktop/personal-dev/map-application/data/original_data/ramen_data_location_51to100.csv',
    '/Users/ogurayuudai/Desktop/personal-dev/map-application/data/original_data/ramen_data_location_101to150.csv'
]

for i, ramen_data_path in enumerate(ramen_data_path_list):
    ramen_data_df = pd.read_csv(ramen_data_path)
    name_list = ramen_data_df['name'].tolist()

    gm = googlemaps.Client(key='AIzaSyA1Sq1-fYP2M2pukwHJ1NsNeHLKDHks_28')

    latitude_list = []
    longitude_list = []
    for name in name_list:
        try:
            res = gm.geocode(name)
            latitude_list.append(res[0]['geometry']['location']['lat'])
            longitude_list.append(res[0]['geometry']['location']['lng'])
        except:
            try:
                res = gm.geocode('ラーメン'+name)
                latitude_list.append(res[0]['geometry']['location']['lat'])
                longitude_list.append(res[0]['geometry']['location']['lng'])
            except:
                latitude_list.append('')
                longitude_list.append('')

    ramen_data_df['latitude'] = latitude_list
    ramen_data_df['longitude'] = longitude_list

    ramen_data_df.to_csv(output_data_path_list[i], index=False)

"""
geolocator = Nominatim(user_agent="test-dayo")
location = geolocator.geocode("中華蕎麦にし乃")
print("Lat, long = ",location.latitude, location.longitude)
print("full address = ", location.address)
"""