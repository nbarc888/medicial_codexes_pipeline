import polars as pl
from pathlib import Path
import pandas as pd
import os

file_path = Path('input\sct2_Description_Full-en_US1000124_20250901.txt')

df =  pl.read_csv(
    file_path,
    separator= ',',
    has_header=True,
    quote_char=None,
    encoding='utf8-lossy',
    truncate_ragged_lines=True,
    dtypes={
        'id': pl.Utf8,
        'effectiveTime': pl.Utf8,
        'active': pl.Int32,
        'moduleId': pl.Utf8,
        'conceptId': pl.Utf8,
        'languageCode': pl.Utf8,
        'typeId': pl.Utf8,
        'term': pl.Utf8,
        
}
)

column = ['id', 'effectiveTime', 'active', 'moduleID', 'conceptId', 'languagecode', 'typeID', 'term', 'caseSignificanceId']

header = ['typeID' , 'term', 'caseSignificanceId' ]


output_dir = Path('output')
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'SNOWMED_Full.csv'

df.write_csv(output_path)
### df.write_csv('snowmed.csv', columns=['typeID' , 'term', 'caseSignificanceId'], index=False)


print(f"Successfully parsed {len(df)} records from SNOMED CT file")
print(f"Saved to {output_path}")
print(f"Dataset shape: {df.shape}")
print(f"\nColumn names: {df.columns}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")

print(f"\nActive terms count: {df.filter(pl.col('active') == 1).height}")
print(f"Language codes: {df['languageCode'].unique().to_list()}")

### employees = [
 ###    {'name': 'Alice', 'department': 'HR'},
  ###  {'name': 'Bob', 'department': 'Engineering'},
  ###  {'name': 'Charlie', 'department': 'HR'}
###]
###headers = ['name', 'department']
###save_to_csv(employees, 'employees.csv', headers)