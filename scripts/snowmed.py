import polars as pl
from pathlib import Path

file_path = Path('medical-codex-pipeline/input/sct2_Description_Full-en_US1000124_20250901.txt')

df =  pl.read_csv(
    file_path,
    separator= '\t',
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
        'caseSignificanceId': pl.Utf8
}
)

import os 

output_dir = Path('medical-codex-pipeline\output')
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'sct2_Description_Full.csv'

df.write_csv(output_path)

print(f"Successfully parsed {len(df)} records from SNOMED CT file")
print(f"Saved to {output_path}")
print(f"Dataset shape: {df.shape}")
print(f"\nColumn names: {df.columns}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")

print(f"\nActive terms count: {df.filter(pl.col('active') == 1).height}")
print(f"Language codes: {df['languageCode'].unique().to_list()}")