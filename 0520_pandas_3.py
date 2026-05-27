import pandas as pd


df1 = pd.DataFrame({
    "Product": ["Apple", "Banana", "Orange", "Mango", "Grape", "Guava"],
    "Price": [30, 20, 25, 60, 45, 35],
    "Sales": [100, 150, 80, 60, 90, 54]
})
print("df1")
print(df1)
data = [
    ["Apple", 30, 100],
    ["Banana", 20, 150],
    ["Orange", 25, 80],
    ["Mango", 60, 60],
    ["Grape", 45, 90],
    ["Guava", 35, 54]
]

df2 = pd.DataFrame(data, columns=["Product", "Price", "Sales"])

print("\ndf2")
print(df2)

print("\nhead() 前5筆資料")
print(df2.head())

print("\ntail() 後5筆資料")
print(df2.tail())

print("\nshape")
print(df2.shape)
print("\ncolumns")
print(df2.columns)

print("\ninfo()")
df2.info()

print("\ndescribe()")
stats = df2.describe().round(2)
print(stats)

stats.to_csv("0520_stock2.csv")

print("\n存檔完成：0520_stock2.csv")
