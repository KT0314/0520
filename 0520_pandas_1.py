import pandas as pd

# 方法一：用 list 建立 Series
stock1 = pd.Series([120, 80, None, 60, 95, None, 110])

print("stock1")
print(stock1)

# 方法二：自訂索引建立 Series
stock2 = pd.Series(
    [120, 80, None, 60, 95, None, 110],
    index=["Apple", "Banana", "Orange", "Mango", "Grape", "Peach", "Melon"]
)

print("\nstock2")
print(stock2)

# 方法三：轉成字典
stock3 = stock2.to_dict()

print("\nstock3")
print(stock3)

# 取值方式
print("\nBanana 庫存：", stock2["Banana"])

# 檢查缺失值
print("\n缺失值檢查：")
print(stock2.isnull())

# 缺失值數量
print("\n缺失值數量：", stock2.isnull().sum())

# 存成 CSV
stock2.to_csv("0520_stock.csv", index=True)

print("\n存檔完成：0520_stock.csv")