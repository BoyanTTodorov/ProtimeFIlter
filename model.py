import os
import pandas as pd

folder_path = r'Data'

folder_data = os.listdir(folder_path)

try:
    df = pd.concat([pd.read_excel(folder_path+'/'+file, engine='openpyxl') for file in folder_data])
    print(df.head())
except Exception as e:
    print(f'Exception occure: {e}')
finally:
    print(f'Data was readed')