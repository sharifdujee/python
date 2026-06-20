import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

'''red_wine_data = pd.read_csv('https://raw.githubusercontent.com/dphi-official/Datasets/master/Wine_Dataset/winequality-red.csv', sep=';')
y = red_wine_data['quality']
x = red_wine_data.drop('quality', axis=1)
#red_wine_data.hist(bins=10, figsize=(16,12))
#plt.show()
plt.figure(figsize=(16,12))
#sns.heatmap(red_wine_data.corr(), annot=True, cmap='bwr')
#sns.countplot(data=red_wine_data, x='quality')
sns.pairplot(red_wine_data)
plt.show()'''

metropolitoan_data = pd.read_csv('http://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv')
'''print(metropolitoan_data.head())
plt.scatter(metropolitoan_data['crime_rate'], metropolitoan_data['percent_senior'])
plt.xlabel('Crime Rate')
plt.ylabel('Percent Senior Citizens')
plt.title('Relationship between Crime Rate and Percent Senior Citizens')'''
plt.figure(figsize=(10,5))
plt.plot(metropolitoan_data['work_force'], metropolitoan_data['income'], color='red', label="Work Force", linestyle="dashed", marker="o", markerfacecolor='blue', markersize=10)
plt.plot(metropolitoan_data['physicians'], metropolitoan_data['income'], label="Physicians",)
plt.title("Add Chart Title")
plt.xlabel("x axis Label")
plt.ylabel("y axis Label")
plt.legend()
plt.show()
#print(metropolitoan_data.head())