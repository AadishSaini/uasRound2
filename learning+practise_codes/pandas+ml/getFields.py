import pandas as pd

filePath = "./Delhi_v2.csv"

file = pd.read_csv(filePath)
file= file.dropna()


arr = file.columns
fields = ['Address', 'area', 'latitude', 'longitude',
       'Bedrooms', 'Bathrooms', 'Balcony', 'Status', 'neworold', 'parking',
       'Furnished_status', 'Lift', 'Landmarks', 'type_of_building', 'desc']

print(arr)