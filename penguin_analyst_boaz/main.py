import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
)

print(f"I have {len(df)} penguins")
print("I have", len(df), "penguins")
