import pandas as pd

data = pd.read_excel("D:\pandas\sample.xlsx")
print(data.head(10)) #head() is used to quickly view the first few rows of a DataFrame for a quick preview.
print(data.tail(10))#tail() is used to quickly view the last few rows of a DataFrame for a quick preview.
#default value is 5
print(data.info())#give inforation about data like datatype etc
print(data.describe())#give describe the data
print(data.isnull())#give null valuses as true
print(data.isnull().sum())