import pandas as  pd
import numpy as np

# pd.set_option("display.max_rows",None)
# pd.set_option("display.max_rows",None)


"""below code is read csv file method"""
# df = pd.read_csv("classification_report.csv")
# print(df)

df = pd.read_csv(r"D:\data science\data_science_newproject\duplicate\classification_report.csv")
print(df)


print(df.head(100))

print(df.tail(10))

print(df[4:15])

print(df[10:20])
print(df[0:])


print(df.loc[4:20,["Curtosis","Skewness"]])

print("----------------------------------------------------")

print(df.iloc[2:20,1:5])
#
# print(df["Skewness"].dtype)
#
# print(df.dtypes)
#
# two_column_data = df[["Class","Entropy","Variance","Curtosis"]]
# print(two_column_data)
#
# column_data = df["Class"]
# # # print(column_data)
#
# b = df.describe()
# print(b)
# #
# df.info()
#
# c = df.shape
# print(c)
#
# d = df.ndim
# print(d)
#
# """removing unwanted column"""
#
# v = df.columns
# print(v)
#
# r = df.drop(columns="Variance",inplace=True)
# print(r)
#
#
# v = df.columns
# print(v)
#
# r1 = df.drop(columns=["Skewness","Entropy"],inplace=True)
# print(r1)
#
# v = df.columns
# print(v)


