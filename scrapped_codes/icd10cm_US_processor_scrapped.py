import pandas as pd 
import re

file_path= 'input\icd10cm_order_2025.txt'

codes = []

with open(file_path, 'r', ecoding='utf-8') as file:
 for line in file:
    
    line = line.rstrip('\n\r')

if len(line) < 15:
continue

order_num = kine[0:5].strip()
code = line[6:13].strip()
level = line[14:15].strip()

remaining_text = line[16:]

parts = re.split(r'\s{4,}', remaining_text, 1)

description = parts[0].strip() if len(parts) > 0 else ""
description_detailed = parts[1].strip() if len(parts) > 1 else ""

codes.append({
            'order_num': order_num,
            'code': code,
            'level': level,
            'description': description,
            'description_detailed': description_detailed
        })

icdcodes = pd.DataFrame(codes)

icdcodes.to_csv("output/icd10cm_order_2025.csv", index=False)