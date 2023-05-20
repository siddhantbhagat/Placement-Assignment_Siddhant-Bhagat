import requests  # to get response from url
import pandas as pd

url = 'https://data.nasa.gov/resource/y77d-th95.json'
json_file_path='json_data_nasa.json'
excel_file_path = 'excel_data_nasa.xlsx'

try:
    response = requests.get(url)

    with open(json_file_path, "wb") as file:
            file.write(response.content)
    
    # Read the JSON file into a pandas DataFrame
    data = pd.read_json(json_file_path)

    # Convert the DataFrame to an Excel file
    data.to_excel(excel_file_path, index=False)

except Exception as e:
      print('Error', e)
