import pandas as pd 
  
# Replace 'output_file.csv' with the actual path to the CSV file


#df_short_file = pd.read_csv('output_file', nrows=50)
#print(df_short_file)



# Codes used below were used to generate shortened csv files created from scripts

### hcpcs
#hcpcs_output_path = ('short_output')
#pd.read_csv('output/hscps_output.csv', nrows=10000, sep=',', header=None).dropna().to_csv('hcpcs_smaller.csv', index=False)
 

### ICD10-US



### ICD10-WHO



### LOINC



### NPI 
## npi_output_path = ('short_output')
## pd.read_csv('output/npi_small.csv', nrows=1000)[['NPI', 'Provider Last Name (Legal Name)']].dropna().to_csv('npi_smaller.csv', index=False)


### RX-Norm



### SNOWMED