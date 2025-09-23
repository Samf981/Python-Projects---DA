import pandas as pd

df = pd.read_csv(r'C:\Users\sferr\Desktop\Curso DATA ANALYST\Python Projects DATA\Python-Projects---DA\Product_sales.csv')

#first 5 rows
df.head()

# Access to the column Length
y=df[['Quantity']]

# Access to column as a series
y1=df['Quantity']

# Get the column or columns as a dataframe
x = df[['Product','Quantity']]
type(x)


# Access the value on the second row and the first column
df.iloc[1,0]

# Access the column using the name
df.loc[1, 'Product']

# Slicing the dataframe
df.iloc[0:2, 0:3]

# Slicing the dataframe
print(df.loc[0:2, 'OrderID':'CustomerCity'])