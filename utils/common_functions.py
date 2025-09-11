import pandas as pd 
  
# Replace 'output_file.csv' with the actual path to the CSV file


#df_short_file = pd.read_csv('output_file', nrows=50)
#print(df_short_file)



# Codes used below were used to generate shortened csv files created from scripts
#please only run one script at a time

### hcpcs
#hcpcs_output_path = ('short_output')
#pd.read_csv('output/hscps_output.csv', nrows=1000, sep=',', header=None).dropna().to_csv('hcpcs_smaller.csv', index=False)
 

### ICD10-US
#icdus_output_path = ('short_output')
#pd.read_csv('output\icd102019_us_beta.csv', nrows=1000, sep=',', header=None).dropna().to_csv('icdus_smaller.csv', index=False)

### ICD10-WHO
#file_path = 'input\icd102019syst_codes.txt'
#columns = [
#           'level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
#          'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
#           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
#           'morbidity_code3', 'morbidity_code4' ]
#header = ['icd10_code', 'parent_title', 'definition']
#df = pd.read_csv(file_path, sep=';', nrows=10000, header=None, names=columns)
#output_path = ('short_output/icdwho_smaller.csv')
#df.to_csv(output_path, columns = header, index=False)

### LOINC

npi_output_path = ('short_output')
pd.read_csv('output\loinc_small.csv', nrows=1000)[['code','description','last_updated']].dropna().to_csv('loinc_smaller.csv', index=False)

### NPI 
## npi_output_path = ('short_output')
## pd.read_csv('output/npi_small.csv', nrows=1000)[['NPI', 'Provider Last Name (Legal Name)']].dropna().to_csv('npi_smaller.csv', index=False)


### RX-Norm



### SNOWMED