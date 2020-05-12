import os, glob 
import pandas as pd 
path = './data'

total_files = glob.glob(os.path.join(path, '*.csv'))
for file in total_files:
    df_merged = pd.read_csv(file)
    df_merged.sort_values(["LED_CODE" , "TRA_DATE"], axis=0, ascending=True, inplace=True)
    splitted_df =df_merged.groupby("LED_CODE")
    for sheet in splitted_df.LED_CODE:
        splitted_df.get_group(sheet[0]).to_csv("./output/"+str(sheet[0])+".csv", index=False, mode='a')
    print('Splitting done for '+ str(file))
print('All splitting done')