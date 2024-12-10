import pandas as pd
import numpy as np

data = pd.read_excel("sample1.xlsx")
print(data.isnull())#if any value is null then it return true in place
print(data.isnull().sum())#give sum of null values present on each coloum
print(data.dropna())#delete row present null value
print(data.replace(np.nan,"empty"))#replace the all null values with word
data["City"] = data["City"].replace(np.nan,"USA")#replace all values of specific coloum_import numpy foroperation
print(data)

print(data["Salary"].mean())#calculate mean of coloum for fill missing values
data["Salary"] = data["Salary"].replace(np.nan, 56400)#replace null with mean value
print(data)

print(data.fillna(method = "bfill"))#fill value present in front
print(data.fillna(method = "ffill"))#fill value present in back