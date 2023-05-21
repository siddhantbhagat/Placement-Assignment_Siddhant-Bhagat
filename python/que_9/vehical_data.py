import pandas as pd
url = 'https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD'
csv_file_path = 'govdata.csv'

try:
    data=pd.read_csv(url)

    # Convert the DataFrame to an csv file
    data.to_csv(csv_file_path, index=False)

except Exception as e:
      print('Error', e)