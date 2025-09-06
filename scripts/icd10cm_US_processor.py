import pandas as pd 
import re

file_path= 'input\icd10cm_order_2025.txt'

codes = []

 with open(file_path, 'r', ecoding='utf-8') as file:
 for line in file:
    
    line = line.rstrip('\n\r')
#### use note++ to look at data stuff :3 consider using claude 
