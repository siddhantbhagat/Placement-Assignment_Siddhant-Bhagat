import requests  # to get response from url
import pandas as pd

url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
excel_file_path = 'episodes.xlsx'

try:
    response = requests.get(url)
    data=response.json()
    data1 = pd.DataFrame(data["_embedded"]["episodes"])

    # Convert the DataFrame to an Excel file
    data1.to_excel(excel_file_path, index=False)

except Exception as e:
      print('Error', e)