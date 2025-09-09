import pandas as pd
import os

file_path = "input/HCPC2025_OCT_ANWEB.txt"

outputStr = "output"
outname = outputStr + "/hscps.csv"
output_directory = outputStr
file_name = outputStr + "/hscps_output.csv"

#### load note use similar icd ruling for columns!!!! note look at note for column descip (0, 11), (11, 90), (90, 180) , (200, 220), ( 220, 240), (240, 260), (260, 280)]
### re tweak the text columns !!!!
###colspecs = [(0, 1), ( 2, 3), (4, 5)]
df = pd.DataFrame({'HCPC Code': [0, 1], 'Long Description': [1, 2], 'Short Description': [2, 3]})

hcpc_column = ['HCPC Code']
long_descript_column = ['Long Description']
short_descript_column = ['Short Description']


### "Unknown1", "Unknown2", "Unknown3", "Unknown4" 
column_names = [
    "HCPC code", " Long Description", "Short Description" 
]
#### clean = df[code, des, etc]
#### clean.to_csv(output)

clean = ["HCPC Code", "Long Description", "Short Description"]

df = pd.read_fwf(file_path)
df.to_csv('output/hscps_output.csv')


df = pd.read_csv('output/hscps_output.csv', skipinitialspace=True)
data_df = pd.read_csv('output\hscps_output.csv')

###specific_columns = [0, 1, 2]
##df = pd.read_csv('output/hscps_output.csv', 
###                 skipcolumns = lambda x:x not in specific_columns)
### print(df)

### optional!!!
### full_path = os.path.join(output_directory, file_name)