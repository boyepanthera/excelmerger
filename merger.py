import os, glob 
import pandas as pd 
path = './data'

total_files = glob.glob(os.path.join(path, '*.csv'))

# df_from_each_file = (pd.read_csv(f, sep=',', header=None, names=columns) for f in total_files)
df_from_each_file = (pd.read_csv(f) for f in total_files)
df_merged   = pd.concat(df_from_each_file)
# df_merged   = pd.concat(df_from_each_file, ignore_index=True, sort=True)
# print(df_merged.head())
df_merged.sort_values(["LED_CODE" , "TRA_DATE"], axis=0, ascending=True, inplace=True)
# print(type(df_merged))
# print(type( df_sorted))
# print(type(df_from_each_file))
splitted_df =df_merged.groupby("LED_CODE")

for sheet in splitted_df.LED_CODE:
    splitted_df.get_group(sheet[0]).to_csv("./output/"+str(sheet[0])+".csv")

# pd.set_option('display.max_columns', None)
# boye = pd.read_csv('./data/trial2.csv' )
# print (boye.head())

print('Splitting done!')