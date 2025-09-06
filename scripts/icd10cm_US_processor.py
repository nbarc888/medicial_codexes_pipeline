import pandas as pd 
import re

file_path= 'input\icd10cm_order_2025.txt'

codes = []

with open(file_path, 'r', ecoding='utf-8') as file:
 for line in file:
    
    line = line.rstrip('\n\r')
#### use note++ to look at data stuff :3 consider using claude 
if len(line) < 15:
continue 

order_num = kine[0:5].strip()
code = line[6:13].strip()
level = line[14:15].strip()