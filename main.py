import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ✅ New working URL (public CSV from GitHub)
url = "https://raw.githubusercontent.com/datasets/job-pay/master/data/job-pay.csv"
df = pd.read_csv(url)

# Show data
print("First few rows:")
print(df.head())

# Simulate 'Remote %'
np.random.seed(42)
df['Remote %'] = np.random.randint(10, 90, size=len(df))

# Clean up
df = df[['job', 'salary', 'Remote %']].dropna()
df['Salary (£k)'] = df['salary'] / 1000
df = df.rename(columns={'job': 'Occupation'})

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(df["Remote %"], df["Salary (£k)"], alpha=0.7)
plt.title("Remote Work vs. Salary (Simulated Example)")
plt.xlabel("Remote Work (%) [Simulated]")
plt.ylabel("Salary (£k)")
plt.grid(True)
plt.tight_layout()
plt.savefig("remote_salary_fixed.png")
plt.show()
