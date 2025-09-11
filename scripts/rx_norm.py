import polars as pl
from pathlib import Path 

file_path= Path('input\RXNATOMARCHIVE.RRF')

# SEE REFERENCE: https://www.nlm.nih.gov/research/umls/rxnorm/docs/techdoc.html#s12_10

columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp', 
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released', 
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]

df = pl.read_csv(
    file_path,
    separator='|',
    has_header=False,
    new_columns=columns,
    truncate_ragged_lines=True
)

output_dir = Path('output')
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'RXNATOMARCHIVE.csv'

df.write_csv(output_path)

print(f"Successfully parsed {len(df)} records from RXNATOMARCHIVE.RRF")
print(f"Saved to {output_path}")
print(f"Dataset shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")

### functional confirmed 