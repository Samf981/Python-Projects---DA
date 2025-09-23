#In this file I will show the comands to clean Datasheet's
# I needed to instal openpyxl in my enviroment through powershell commands
import pandas as pd

#Read excel file
dataframe_name = pd.read_excel("Car_Sales.xlsx")

#Write Excel file to CSV
dataframe_name.to_csv("output.csv", index=False)

dataframe_name["Sales"] # Accesses single column
dataframe_name[["Quantity", "Sales"]] # Accesses multiple columns

dataframe_name.describe()   #Statistics: Count, ean, std,min...

#Remove columns
#dataframe_name.drop(["column1", "column2"], axis=1, inplace=True)   
#dataframe_name.drop(index=[row1, row2], axis=0, inplace=True)


#Remove rows with missing NAN vakus (axis=0 indicates rows)
#dataframe_name.dropna(axis=0, inplace=True)

#shows table with True or false. If row false, then it is unique
dataframe_name.duplicated()

#Creates a new DataFrame with rows that meet specified conditions.
New_DF = dataframe_name[(dataframe_name["Quantity"] > 2) & (dataframe_name["Sales"] < 50000)]

#Group Dataframe to work a dataset
#grouped = dataframe_name.groupby(["category", "region"]).agg({"sales": "sum"})

#Merge 2 datasets
#merged_df = pd.dataframe_name(sales, products, on=["product_id", "category_id"])

#Replace values in collumn
#dataframe_name["column_name"].replace(old_value, new_value, inplace=True)

#######NUMPY###############################

import numpy as np
list1=[1,2,3,4,5]
list2=(10,11,12,13,14)
array_1d = np.array([list1]) # 1D Array
array_2d = np.array([[list1], [list2]]) # 2D Array

#Math Functions
np.mean(array_1d)
np.sum(array_1d)
np.min(array_1d)
np.max(array_1d)
#np.dot(array_1d,array_2)

X=np.array([[1,0,1],[2,2,2]])
print(X.ndim)