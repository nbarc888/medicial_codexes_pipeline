import pandas as pd 

loinc = pd.read_csv('input\Loinc.csv')

loinc.iloc[0]

loinc.info()

loinc.STATUS.value_counts
loinc.CLASSTYPE.value_counts

loinc.LOINC_NUM
loinc.LONG_COMMON_NAME


list_cols = ['LOINC_NUM', 'LONG_COMMON_NAME', 'VersionLastChanged']
print('list_cols')

subset = loinc[list_cols]
print(subset.head())

loinc_small = loinc[['LOINC_NUM', 'LONG_COMMON_NAME', 'VersionLastChanged']]
loinc_small = loinc[list_cols]

'LOINC_NUM'=='code'
'LONG_COMMON_NAME'=='description'
'VersionLastChanged'=='last_updated'

loinc_small = loinc_small.rename(columns={
    'LOINC_NUM': 'code',
    'LONG_COMMON_NAME': 'description',
    'VersionLastChanged' : 'last_updated'
})

file_output_path = 'loinc_small.csv'

loinc_small.to_csv('output/loinc_small.csv')

### FUNCTIONALITY CONFIRMED