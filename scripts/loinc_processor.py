import pandas as pd 

loinc = pd.read_csv('input\Loinc.csv')

loinc.iloc[0]

loinc.info()

loinc.STATUS.value_counts
loinc.CLASSTYPE.value_counts

loinc.LOINC_NUM
loinc.LONG_COMMON_NAME


list_cols = ['LOINC_NUM', 'DefinitionDescription']
print('list_cols')

subset = loinc[list_cols]
print(subset.head())

loinc_small = loinc[['LOINC_NUM', 'LONG_COMMON_NAME']]
loinc_small = loinc[list_cols]

'LOINC_NUM'=='code'
'LONG_COMMON_NAME'=='description'
'last_updated'=='last_updated'