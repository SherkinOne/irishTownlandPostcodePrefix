import csv
import json
 
fileName= 'C:\\Users\KM\\Desktop\\osm_townlands.json'

# Open the JSON file
with open(fileName, 'r', encoding='utf-8')  as file:
    # Load the JSON data into a Python object
    data = json.load(file)
    
county_features = {}

for feature in data["features"]:
    co_name = feature["properties"]["CO_NAME"]
    if co_name not in county_features:
        county_features[co_name] = []
    county_features[co_name].append(feature)

for co_name, features in county_features.items():
    filename = f"C:\\Users\KM\\Desktop\\townlandGeojson\\{co_name}_townlands.json"
    with open(filename, "w", encoding='utf-8')  as file:
        output={"type":"FeatureCollection", "features": features}
        json.dump( output, file)
