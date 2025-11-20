import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Task 5\effects-of-covid-19-on-trade.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")

print(" FIRST 5 ROWS")
print(df.head())



yearly = df.groupby(["Year", "Direction"])["Value"].sum()
print("\n Total Trade Value by Year & Direction:")
print(yearly)

plt.figure(figsize=(8,5))
yearly.unstack().plot(kind="bar")
plt.title("Yearly Trade Value (Exports vs Imports)")
plt.xlabel("Year")
plt.ylabel("Total Value")
plt.grid(True)
plt.show()


transport = df.groupby("Transport_Mode")["Value"].sum()

plt.figure(figsize=(8,5))
transport.plot(kind="pie", autopct="%1.1f%%")
plt.title("Trade Share by Transport Mode")
plt.ylabel("")
plt.show()

daily = df.groupby("Date")["Value"].sum()

plt.figure(figsize=(10,5))
daily.plot(kind="line")
plt.title("Daily Trade Value Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Value")
plt.grid(True)
plt.show()

direction_total = df.groupby("Direction")["Value"].sum()

plt.figure(figsize=(8,5))
direction_total.plot(kind="bar", color=["skyblue", "salmon"])
plt.title("Total Import vs Export Value")
plt.xlabel("Direction")
plt.ylabel("Value")
plt.grid(True)
plt.show()

print("Done Ananlysis")
