import pandas as pd

df = pd.read_csv("data/raw/PS_20174392719_1491204439457_log.csv")
print(df.shape)
print(df["type"].value_counts())
print(df.groupby("type")["isFraud"].agg(["sum", "mean"]))
print("overall fraud rate:", df["isFraud"].mean())

df["drains_account"] = (df["newbalanceOrig"] == 0) & (df["amount"] > 0)
print(df.groupby("isFraud")["drains_account"].mean())
