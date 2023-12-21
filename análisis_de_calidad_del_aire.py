import pandas as pd
import requests
url = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
data = pd.read_csv(url, sep=';')
city = data['City'].drop_duplicates().tolist()
df = pd.DataFrame(columns=['ciudad','CO', 'NO2', 'O3', 'SO2', 'PM2.5', 'PM10', 'overall_aqi'])
ind = 0 

for ciudad in city :
    api_url = f'https://api.api-ninjas.com/v1/airquality?city={ciudad}'
    response = requests.get(api_url, headers={'X-Api-Key': 'ksaRxSR8zkQMNkg09ITXxA==rnPYuiqeJYcZKf17'})
    if response.status_code == requests.codes.ok:
        datos = response.json()
        row = [ciudad, datos['CO']["concentration"], datos['NO2']["concentration"], datos['O3']["concentration"], datos['SO2']["concentration"], datos['PM2.5']["concentration"], datos['PM10']["concentration"], datos['overall_aqi']]
        df.loc[len(df)] = row

print(df.head(10))