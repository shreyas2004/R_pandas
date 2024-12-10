import pandas as pd

data = pd.read_excel("sample1.xlsx")
# print(data)

print(data.duplicated())#finds duplicate in first coloum
print(data["Age"].duplicated())#finds in given  coloum
print(data["Age"].duplicated().sum())#give total num of duplicates
print(data.drop_duplicates("Age"))#drops the row contain duplicates