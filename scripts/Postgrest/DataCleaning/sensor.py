import requests
import pandas as pd
import numpy as np
from dotenv import dotenv_values
import geopandas as gpd
config = dotenv_values(".env") #apikey

station = {
    "stationname":"sniffer",
    "projectid":"SETx-UIFL Beaumont",
    "description": "Beaumont Run of the SNIFFER air quality sensor for VOCUS data",
    "contactname": "Pawell",
    "contactemail": "Pawell@utexas.edu",
    "active":True,
    "startdate": "Feb 23, 2023 17:05:57",
    "datetime": "Feb 25, 2023 12:18:11"
}
# r = requests.post("https://postgrest-dev.proudflower-a6582e11.centralus.azurecontainerapps.io/station", headers={'Authorization': f'Bearer {config["apikey"]}',
#          }, data=station)
# print(r)




MassList = pd.read_csv("2023Beaumont_partial/w_data/Export/UL/IonList/MassIDs_2023.02.23-17h36m01sUL.csv", header=None)
sensor = np.fromfile("2023Beaumont_partial/w_data/Export/UL/CPS/cps2023.02.23-17h36m01sUL.fdt", sep="\n")
engData = np.fromfile("2023Beaumont_partial/w_data/Export/EngData/EngData2023.02.23-17h36m01s.fdt",sep="\n")
with open ("2023Beaumont_partial/w_data/Export/EngData/EngDataNames2023.02.23-17h36m01s.csv" , encoding="ISO-8859-1") as f:
    engDataNames = (f.read().split("\n"))

sensor_table = pd.DataFrame({"alias": MassList[0].tolist()})
sensor_table['postprocess'] = True
sensor_table['postprocessscript'] = None
sensor_table['units'] = 'Counts Per Second'
sensor_table['datatype'] = 1


r = requests.get("https://postgrest-dev.proudflower-a6582e11.centralus.azurecontainerapps.io/station?projectid=eq.SETx-UIFL Beaumont&stationname=eq.sniffer")
sensor_table['stationid']= r.json()[0]['stationid']


# r = requests.post("https://postgrest-dev.proudflower-a6582e11.centralus.azurecontainerapps.io/sensor", headers={'Authorization': f'Bearer {config["apikey"]}',
#          'Content-Type':'text/csv'}, data=sensor_table.to_csv(header=True, index=False))
