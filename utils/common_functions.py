import pandas as pd 
  
# Replace 'output_file.csv' with the actual path to the CSV file


df_short_file = pd.read_csv('output_file', nrows=50)
print(df_short_file)