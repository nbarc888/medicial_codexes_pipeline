import pandas as pd

file_path = 'input\icd102019syst_codes.txt'

columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code']

df = pd.read_csv(file_path, sep=';', header=None, names=columns)

output_path = ('output/icd102019syst_codes.csv')
df.to_csv(output_path, index=False)

print(f"Successfully parsed {len(df)} records from {file_path}")
print(f"Saved to {output_path}")
print(f"\nFirst 5 rows:")
print(df.head())