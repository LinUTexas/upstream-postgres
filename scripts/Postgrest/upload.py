import requests
import pandas as pd

MassList = pd.read_csv("2023Beaumont_partial/w_data/Export/UL/IonList/MassIDs_2023.02.23-17h36m01sUL.csv")


class Beaumont_air:
    def __init__(self, URL="https://postgrest-dev.proudflower-a6582e11.centralus.azurecontainerapps"):
        self.api_url = URL
        self.measurement_df = measurement_df
        self.station = station
        self.sensor_table = sensor_table

    
    def load_table(self):
        url = f"{self.base_url}/{self.table_name}"
        response = requests.get("https://postgrest-dev.proudflower-a6582e11.centralus.azurecontainerapps")
        self.data = response.json()
        response.raise_for_status()

    def store_table(self):
        url = f"{self.base_url}/{self.table_name}"
        response = requests.post(url, json=self.data)
        response.raise_for_status()


def upload_table(self):
    self.store_table()


def upload_csv(self, ("2023Beaumont_partial/w_data/Export/UL/IonList/MassIDs_2023.02.23-17h36m01sUL.csv"

):
df = pd.read_csv(("2023Beaumont_partial/w_data/Export/UL/IonList/MassIDs_2023.02.23-17h36m01sUL.csv")
self.data = df.to_dict(orient='records')
self.store_table()


def open_csv(self, ("2023Beaumont_partial/w_data/Export/UL/IonList/MassIDs_2023.02.23-17h36m01sUL.csv"

):
df = pd.read_csv(("2023Beaumont_partial/w_data/Export/UL/IonList/MassIDs_2023.02.23-17h36m01sUL.csv")
self.data = df.to_dict(orient='records')
