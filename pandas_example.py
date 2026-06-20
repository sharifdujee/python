import pandas as pd
'''l = [1,1, 2,3,5,8,13]
s = pd.Series(l)
print(s)

data = [[1000, "Alice", 101.52], 
        [1001, "Bob", 99.99],
        [1002, "Charlie", 150.00],
        [1003, "David", 120.75],
        [1004, "Eve", 110.25]]
df = pd.DataFrame(data, columns=['ID', "Name", "Balance"], index=[1,2,3,4,5])
print(df)'''
#student_data = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/exam_scores.csv")
#sma_data = pd.read_csv('https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv')
#sma_data = pd.read_csv('https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv')

#print(sma_data.info())
'''indexing = sma_data.iloc[0:5, 4]
print(indexing)
print(sma_data.describe(include='all'))
print(sma_data['region'].value_counts())
print(sma_data.mean())'''
#print(sma_data['region'].unique())
#print(sma_data.describe())
#print(sma_data.sort_values(by='crime_rate', ascending=False).head())


titanic_data = pd.read_csv(
    'https://raw.githubusercontent.com/aiplanethub/Datasets/master/titanic_data.csv'
)

print(titanic_data.isnull())
