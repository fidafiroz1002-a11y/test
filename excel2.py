import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("book2.csv")

print(df)

plt.bar(df["names"],df["total"])
plt.xlabel("Names")
plt.ylabel("Marks")
plt.title("Student Marks Graph")
plt.show()