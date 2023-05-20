import requests  # to get response from url
import pandas as pd

url = 'https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json'
json_file_path='json_data.json'
excel_file_path = 'excel_data.xlsx'

try:
    response = requests.get(url)

    data=response.json()
    data1 = pd.DataFrame(data['pokemon'])

    # Convert the DataFrame to an Excel file
    data1.to_excel(excel_file_path, index=False)

except Exception as e:
      print('Error', e)
