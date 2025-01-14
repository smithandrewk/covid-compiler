import os
import pandas as pd

# Find all directories that contain 'FastaFile' in their name
dirs = [file for file in os.listdir('.') if 'FastaFile' in file]

# Initialize an empty list to store DataFrames
df_list = []

# Loop through each directory, read the CSV, and append it to the list
for dir in dirs:
    csv_path = os.path.join(dir, 'lineage_report.csv')
    df = pd.read_csv(csv_path)
    df = df[['taxon', 'lineage']]
    df_list.append(df)
    print(f'{len(df)} new sequences from {dir}')

# Concatenate all DataFrames into one
final_df = pd.concat(df_list, ignore_index=True)

log = pd.read_excel(f'2024_COVID-19_sequencing_log.xlsx')
log = log.set_index('Key').loc[final_df['taxon'].to_list()]
print(f'{len(log)} found in log')
log
# if not equal big error

final_df = final_df.rename({'taxon':'Key'},axis=1).set_index('Key')

# Display the concatenated DataFrame
print(f'Total sequences: {len(final_df)}')

log['Variant'] = final_df['lineage']
log['Category (VOI/VOC/other)'] = 'VOC'
log['WHO Nomenclature '] = ''
log['Variant Description'] = ''
log['Disease Onset Date'] = ''
log['Notes'] = ''
log['Lab'] = 'PHL'
log = log.rename({'PATIENT NAME':'NAME','OPENELIS ACCESSION #':'OE #',"Date Rcd\'v in Molecular":'Date Discovered/Recieved'},axis=1)
tmp = log[['Variant', 'WHO Nomenclature ', 'Variant Description','Category (VOI/VOC/other)', 'NAME', 'DOB', 'SEX', 'RACE', 'COUNTY','STATE', 'DOC', 'AGE', 'Disease Onset Date', 'OE #', 'Notes', 'Lab','Date Discovered/Recieved']]
tmp['DOB'] = tmp['DOB'].astype('datetime64[ns]')
tmp.to_csv(f'01_14_2025_Variants.csv',index=False)