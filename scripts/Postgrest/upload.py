import os

import requests
import pandas as pd
from dotenv import dotenv_values
config = dotenv_values(".env") #apikey

# MassList = pd.read_csv("2023Beaumont_partial/w_data/Export/UL/IonList/MassIDs_2023.02.23-17h36m01sUL.csv")


class UPStreamLibrary:
    def __init__(self, api_url="https://postgrest-dev.proudflower-a6582e11.centralus.azurecontainerapps.io"):
        self.api_url = api_url
        self.header = {'Authorization': f'Bearer {config["apikey"]}'}
        self.measurement_df = self.load_table_csv(
            "DataCleaning/cleanData/sensor.csv")
        self.Station_Metadata={}
        # self.station = station
        # self.sensor_table = sensor_table

    def load_table_csv(self, csv_location):
        return pd.read_csv(csv_location)
    def GET_table(self, table_name):
        url = os.path.join(self.api_url, table_name)
        response = requests.get(url)
        self.data = response.json()
        print(self.data)
        response.raise_for_status()

    def POST_table(self, table_name):
        url = f"{self.api_url}/{table_name}"
        response = requests.post(url, json=self.data)
        response.raise_for_status()


if __name__== '__main__':
    sniffer = UPStreamLibrary(
        api_url="http://postgrest-dev.proudflower-a6582e11.centralus"
                ".azurecontainerapps.io")
    sniffer.Station_Metadata = {
    "stationname":"sniffer_test",
    "projectid":"SETx-UIFL Beaumont",
    "description": "Beaumont Run of the SNIFFER air quality sensor for VOCUS data",
    "contactname": "Pawell",
    "contactemail": "Pawell@utexas.edu",
    "active":True,
    "startdate": "Feb 23, 2023 17:05:57",
    "datetime": "Feb 25, 2023 12:18:11"
}

    sniffer.GET_table("station?projectid=eq.SETx-UIFL%20Beaumont&stationname=eq.sniffer")
    #Post Thee Data

    sniffer.GET_table("station?projectid=eq.SETx-UIFL%20Beaumont&stationname=eq.sniffer_test")

    pass
#
# def upload_table(self):
#     self.store_table()
#
#
# def upload_csv(self, "2023Beaumont_partial/w_data/Export/UL/IonList/MassIDs_2023.02.23-17h36m01sUL.csv"):
#     df = pd.read_csv(("2023Beaumont_partial/w_data/Export/UL/IonList/MassIDs_2023.02.23-17h36m01sUL.csv")
#     self.data = df.to_dict(orient='records')
#     self.store_table()
#
#
# def open_csv(self, "2023Beaumont_partial/w_data/Export/UL/IonList/MassIDs_2023.02.23-17h36m01sUL.csv"):
#     df = pd.read_csv(("2023Beaumont_partial/w_data/Export/UL/IonList/MassIDs_2023.02.23-17h36m01sUL.csv")
#     self.data = df.to_dict(orient='records')
