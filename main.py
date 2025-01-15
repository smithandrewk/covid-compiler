import os
import pandas as pd

# Find all directories that contain 'FastaFile' in their name
dirs = [file for file in os.listdir('.') if 'FastaFile' in file]

# Loop through each directory, read the lineage_report CSV, and append it to the list
lab_id_to_covid_lineage_df = pd.concat([pd.read_csv(os.path.join(dir, 'lineage_report.csv'))[['taxon', 'lineage']] for dir in dirs],ignore_index=True)

log = pd.read_excel(f'2024_COVID-19_sequencing_log.xlsx')
log = log.set_index('Key').loc[lab_id_to_covid_lineage_df['taxon'].to_list()]
lab_id_to_covid_lineage_df = lab_id_to_covid_lineage_df.rename({'taxon':'Key'},axis=1).set_index('Key')
print(f'{len(log)} found in log')

log['Variant'] = lab_id_to_covid_lineage_df['lineage']
log['Category (VOI/VOC/other)'] = 'VOC'
log['WHO Nomenclature '] = ''
log['Variant Description'] = ''
log['Disease Onset Date'] = ''
log['Notes'] = ''
log['Lab'] = 'PHL'
log = log.rename({'PATIENT NAME':'NAME','OPENELIS ACCESSION #':'OE #',"Date Rcd\'v in Molecular":'Date Discovered/Recieved'},axis=1)

final_csv_to_send = log[['Variant', 'WHO Nomenclature ', 'Variant Description','Category (VOI/VOC/other)', 'NAME', 'DOB', 'SEX', 'RACE', 'COUNTY','STATE', 'DOC', 'AGE', 'Disease Onset Date', 'OE #', 'Notes', 'Lab','Date Discovered/Recieved']]
final_csv_to_send['DOB'] = final_csv_to_send['DOB'].astype('datetime64[ns]')

final_csv_to_send.to_csv(f'01_14_2025_Variants.csv',index=False)