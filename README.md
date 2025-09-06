# medical-codex-pipeline
507 HHA Assignment- Please review :https://github.com/hantswilliams/HHA-507-2025/blob/main/assignments/assignment1_medicalcodexes.md for further information 


Goal is to create a repo which includes information on 7 different medical codexes

### List of Codexes
| Codex | Focus |
|--------|---------|
| SNOWMED CT (US) | Clinical Terminology |
| ICD-10-CM (US)| Diagnosis Codes |
| ICD-10 (WHO) | International Diagnosis Codes|
| HCPCS (US) | Healthcare Procedure Codes |
| LOINC (US) | Laboratory Test Codes|
| RxNorm (US) | Medication Codes|
| NPI (US) | Healthcare Provider Identifiers |

Keep in reference: 
Please use standard column names across all codexes 
Code : Primary ID
Description: Human-readable description
Last_Updated : Processing timestamp of when product was last updated

### Also Utilize 
Create 'utils/common_functions.py'
'for save_to_formats(df, Base_filename)' : to save DataFrame to CSV 
