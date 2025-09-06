import pandas as pd
import os

file_path = "input/HCPC2025_OCT_ANWEB.txt"

outname = "output/hscps.csv"
output_directory = "output"
file_name = "output/hscps_output.csv"

#### load note use similar icd ruling for columns!!!! note look at note for column descip
### re tweak the text columns !!!!
colspecs = [(0, 11), (11, 90), (90, 180), (180,200), (200, 220), ( 220, 240), (240, 260), (260, 280)]
column_names = [
    "code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"
]
#### clean = df[code, des, etc]
#### clean.to_csv(output)

df = pd.read_fwf(file_path, colespecs= colspecs, names = column_names)
df.to_csv('output/hscps_output.csv')

### optional!!!
full_path = os.path.join(output_directory, file_name)