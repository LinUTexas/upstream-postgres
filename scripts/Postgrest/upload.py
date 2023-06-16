import os
import json
import requests
import pandas as pd
from dotenv import dotenv_values
config = dotenv_values("scripts/Postgrest/.env") #apikey

with open("scripts/Postgrest/DataCleaning/cleanData/schema.json") as f: 
    args = json.loads(f.read())[0]


class UPStreamLibrary:
    def __init__(self,data_dir, api_url):
        self.api_url = api_url
        self.header = {'Authorization': f'Bearer {config["apikey"]}'}
     
        self.Station_Metadata={}
        self.sensor_table = self.load_table_csv(data_dir, "sensor.csv")
        self.measurement_table = self.load_table_csv(data_dir, "measurement.csv")


    def load_table_csv(self, csv_dir, csv_file):
        return pd.read_csv(os.path.join(csv_dir, csv_file))
    
    def GET_table(self, table_name):
        url = os.path.join(self.api_url, table_name)
        response = requests.get(url)
        self.data = response.json()

        response.raise_for_status()

    def UPSERT_table(self, table_name, query_column, id, data):
        self.GET_table(f"{table_name}?{query_column}=eq.{id}")
        
        data[f'{table_name}id'] = (self.data[0])[f'{table_name}id']
        url = f"{self.api_url}/{table_name}"
    
        print(data)
        response = requests.post(url,
        headers={'Authorization': f'Bearer {config["apikey"]}',
                    "Prefer": "resolution=merge-duplicates"},
        data=data)
             
    def POST_table(self, table_name, data):
        url = f"{self.api_url}/{table_name}"
        if type(data) is dict:
            print(data)
            response = requests.post(url,
            headers={'Authorization': f'Bearer {config["apikey"]}',
                     "Prefer": "return=representation"},
            data=data)
        else: 
            response = requests.post(url,
            headers={'Authorization': f'Bearer {config["apikey"]}','Content-Type':'text/csv',
                     "Prefer": "return=representation"},
            data=data)
        return response


if __name__== '__main__':
    print(os.getcwd())
   
    sniffer = UPStreamLibrary(data_dir=args['data_dir'],
        api_url=args['url'])
    
    sniffer.Station_Metadata = args['metadata']

    sniffer.UPSERT_table('station','projectid', "SETx-UIFL Beaumont", sniffer.Station_Metadata)

    for m in sniffer.sensor_table['alias'].tolist():
        print(m)
        sniffer.measurement_table['measurementvalue'] = sniffer.measurement_table[f'{m}']
        data = sniffer.POST_table('sensor', sniffer.sensor_table.loc[sniffer.sensor_table['alias']==m].to_dict("records")[0])
        sniffer.measurement_table['sensorid'] = json.loads(data.text)[0]['sensorid']

        data = sniffer.POST_table('measurement?select=collectiontime,geometry,measurementvalue,sensorid',
                                   sniffer.measurement_table[['sensorid','collectiontime', 'geometry', 'measurementvalue'  ]].to_csv(header=True, index=False)
        )
        

    
