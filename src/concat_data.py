import pandas as pd

ramen_data_df1 = pd.read_csv('ramen_data1to1.csv')
ramen_data_df50 = pd.read_csv('ramen_data1to50.csv')

ramen_data_df123 = pd.DataFrame({'name': ['らぁ麺 飯田商店 湯河原本店', '中華蕎麦 とみ田', '麺屋吉左右'],
                                 'rank': ['1', '2', '3'],
                                 'point': ['99.743', '99.676', '99.575']})
df = pd.concat([ramen_data_df123, ramen_data_df1])
df1 = pd.concat([df, ramen_data_df50])

df1.to_csv(f"ramen_data1to50.csv", index=False)