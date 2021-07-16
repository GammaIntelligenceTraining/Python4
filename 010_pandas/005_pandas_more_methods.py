import pandas as pd

df = pd.read_csv('csv_files//2019.csv')

# # iterrows() method will create an iterable object from rows
# for index, row in df.iterrows():
#     print(index, row)
#     print(row['Country or region'])
#

# Print row with condition
print(df.loc[df['Country or region'] == 'Estonia'])

# Description of dataframe
print(df.describe())

# Sorting by column
print(df.sort_values('Country or region', ascending=True))
print(df.sort_values(['GDP per capita', 'Generosity'], ascending=False))
print(df.sort_values(['Country or region', 'Generosity'], ascending=[1, 0]))

# Sum columns to a new one
df['Total'] = df['GDP per capita'] + df['Generosity'] + df['Perceptions of corruption']
print(df['Total'])

# Delete column from dataframe
df = df.drop(columns=['Total'])
print(df)

print(df.dtypes)

# Contains
print(df.loc[df['Country or region'].str.contains('on | an')])

new_df = pd.read_csv('csv_files//test.csv')
print(new_df)

print(df.loc[df['GDP per capita'] < 1, ['Country or region']])

print(df.groupby('GDP per capita').mean().sort_values('Score', ascending=False))

print(df.groupby('GDP per capita').sum())


print(df.groupby('GDP per capita').count())
print(df.groupby('GDP per capita').count()['Score'])

# Working with large data
for df in pd.read_csv('csv_files//2019.csv', chunksize=5):
    print('Chunk')
    print(df)

