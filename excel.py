import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("marks.csv")

print(df)

plt.bar(df["names"],df["marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Graph")
plt.show()
plt.scatter(df["names"],df["marks"])
plt.show()