import os
import pandas as pd

folder_path = r'Data'

folder_data = os.listdir(folder_path)

try:
    df = pd.concat([pd.read_excel(folder_path+'/'+file, engine='openpyxl') for file in folder_data if file.endswith('.xlsm') or file.endswith('.xlsx')])
    mask = df['Jobcode'].str.startswith('26')
    filtered_df = df[mask].copy()
    filtered_df.columns
    filtered_df = filtered_df.rename(columns = {})
    filtered_df.to_excel('guess.xlsx',index=False)
except Exception as e:
    print(f'Exception occure: {e}')
finally:
    print(f'Data was filtered')

    