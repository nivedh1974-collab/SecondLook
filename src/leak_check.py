import pandas as pd

df = pd.read_csv("data/raw/PS_20174392719_1491204439457_log.csv")
sub = df[df["type"].isin(["TRANSFER", "CASH_OUT"])].copy()
sub["drains_account"] = (sub["newbalanceOrig"] == 0) & (sub["amount"] > 0)
print(sub.groupby(["type", "isFraud"])["drains_account"].mean())
print(sub.groupby("isFraud")["amount"].median())
