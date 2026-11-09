from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "service_demand_synthetic.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["month"])

# Basic validation and cleaning
required = [
    "month", "region", "requests_received", "requests_completed",
    "open_requests_end_month", "overdue_requests", "median_wait_days"
]
missing_columns = sorted(set(required) - set(df.columns))
if missing_columns:
    raise ValueError(f"Missing required columns: {missing_columns}")

quality = []
for col in required:
    quality.append({
        "check": f"{col}: missing values",
        "result": int(df[col].isna().sum()),
        "status": "PASS" if df[col].isna().sum() == 0 else "REVIEW"
    })

for col in ["requests_received", "requests_completed", "open_requests_end_month",
            "overdue_requests", "median_wait_days"]:
    negative = int((df[col] < 0).sum())
    quality.append({
        "check": f"{col}: negative values",
        "result": negative,
        "status": "PASS" if negative == 0 else "REVIEW"
    })

df["completion_rate_pct"] = (
    df["requests_completed"] / df["requests_received"].replace(0, pd.NA) * 100
).round(1)
df["net_demand"] = df["requests_received"] - df["requests_completed"]

monthly = (df.groupby("month", as_index=False)
             .agg(requests_received=("requests_received", "sum"),
                  requests_completed=("requests_completed", "sum"),
                  open_requests=("open_requests_end_month", "sum"),
                  overdue_requests=("overdue_requests", "sum"),
                  median_wait_days=("median_wait_days", "median")))
monthly["completion_rate_pct"] = (
    monthly["requests_completed"] / monthly["requests_received"] * 100
).round(1)
monthly["net_demand"] = monthly["requests_received"] - monthly["requests_completed"]
monthly.to_csv(OUT / "monthly_kpis.csv", index=False)

regional = (df.groupby("region", as_index=False)
              .agg(requests_received=("requests_received", "sum"),
                   requests_completed=("requests_completed", "sum"),
                   avg_open_requests=("open_requests_end_month", "mean"),
                   avg_overdue_requests=("overdue_requests", "mean"),
                   median_wait_days=("median_wait_days", "median")))
regional["completion_rate_pct"] = (
    regional["requests_completed"] / regional["requests_received"] * 100
).round(1)
regional.to_csv(OUT / "regional_summary.csv", index=False)

pd.DataFrame(quality).to_csv(OUT / "data_quality_checks.csv", index=False)

print("Analysis complete. Outputs saved to:", OUT)
print("\\nLatest month:")
print(monthly.tail(1).to_string(index=False))
print("\\nRegions with highest average open requests:")
print(regional.nlargest(5, "avg_open_requests")[
    ["region", "avg_open_requests", "completion_rate_pct", "median_wait_days"]
].to_string(index=False))
