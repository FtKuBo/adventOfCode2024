import pandas as pd

data = pd.read_csv('input.txt', sep='\s+', names = ['col1', 'col2'])

df1 = data['col1'].sort_values().reset_index(drop = True)
df2 = data['col2'].sort_values().reset_index(drop = True)

df_diff = (df1 - df2).abs()

print('total distance :', df_diff.sum(axis=0, skipna=True))

ids = set(df1)
similarityScore = 0

for row in df2:
    if row in ids : similarityScore +=row

print('similarity score :', similarityScore)
