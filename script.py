import pandas as pd

df = pd.read_csv("data/dataset.csv")

print("Dataset preview:")
print(df.head())

print("\nstatistic:")
print(df.describe())


