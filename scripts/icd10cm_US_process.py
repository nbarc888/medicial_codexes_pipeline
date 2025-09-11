import pandas as pd
import os 

file_path = 'input\icd10cm_order_2025.txt'

###columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
##           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
##           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
##           'morbidity_code3', 'morbidity_code4']

colspecs = [(0, 5), (5, 13), (14, 15), (16,200)]
column_names = [
          'order_num', 'code', 'level', 'description'
           ]

header = [
'order_num', 'code', 'description'
]

df = pd.read_fwf(file_path, colspecs=colspecs, seperate=",", names=column_names)

output_path = ('output/icd102019_us_beta.csv')
df.to_csv(output_path, index=False)

# CONFIRMED FUNCTIONAL