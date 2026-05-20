import pandas as pd

# =========================
# 方法一：用字典建立 DataFrame
# =========================
df1 = pd.DataFrame({
    "Product": ["Apple", "Banana", "Orange", "Mango", "Grape", "Guava"],
    "Price": [30, 20, 25, 60, 45, 35],
    "Sales": [100, 150, 80, 60, 90, 54]
})

print("df1")
print(df1)

# =========================
# 方法二：用列表（子列表）建立 DataFrame
# =========================
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

# =========================
# 查看前5筆資料
# =========================
print("\nhead() 前5筆資料")
print(df2.head())

# =========================
# 查看後5筆資料
# =========================
print("\ntail() 後5筆資料")
print(df2.tail())

# =========================
# 查看列數與欄數
# =========================
print("\nshape")
print(df2.shape)

# =========================
# 查看欄位名稱
# =========================
print("\ncolumns")
print(df2.columns)

# =========================
# 查看 DataFrame 基本資訊
# =========================
print("\ninfo()")
df2.info()

# =========================
# 查看數值統計資訊
# =========================
print("\ndescribe()")
stats = df2.describe().round(2)
print(stats)

# =========================
# 存成 CSV 檔
# =========================
stats.to_csv("0520_stock2.csv")

print("\n存檔完成：0520_stock2.csv")