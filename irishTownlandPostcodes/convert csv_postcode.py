import csv
import json

counties = [
    
    "Carlow",
    "Cavan",
    "Clare",
    "Cork",
    "Donegal",
    "Dublin",
    "Galway",
    "Kerry",
    "Kildare",
    "Kilkenny",
    "Laois",
    "Leitrim",
    "Limerick",
    "Longford",
    "Louth",
    "Mayo",
    "Meath",     
    "Offlay",
    "Roscommon",
    "Sligo",
    "Tipperary",
    "Waterford",
    "Westmeath",
    "Wexford",
    "Wicklow"
];




for county in counties:
    data = {}
    countyFile= 'C:\\Users\KM\\Documents\\'+county+'.csv'
    # Read CSV file
    with open(countyFile, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            town = row[0]
            postcode = row[1]
            if postcode in data:
                data[postcode].append(town)
            else:
                data[postcode] = [town]

    # Convert data to JSON
    json_data = json.dumps(data)

    # Save each postcode as a separate JSON file
    for postcode, towns in data.items():
        json_data = json.dumps({postcode: towns})
        filename = f"C:\\Users\KM\\Documents\\postCodeFiles\\{postcode}.json"
        with open(filename, "w") as file:
            file.write(json_data)
