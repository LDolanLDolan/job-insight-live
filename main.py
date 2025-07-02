# main.py
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 📊 Load live UK salary data from ONS (ASHE 2023)
url = "https://www.ons.gov.uk/file?uri=/employmentandlabourmarket/peopleinwork/earningsandworkinghours/datasets/occupationbyfulltimeweeklyearningsashetable14/2023provisional/table142023provisional.csv"
df = pd.read_csv(url, skiprows=4)

# 🧼 Clean and simplify
df = df.rename(columns={df.columns[0]: 'Occupation', df.columns[1]: 'Weekly Pay (£)'})
df = df[['Occupation', 'Weekly Pay (£)']].dropna()

# 🎲 Add simulated Remote Work % (since not in this dataset)
np.random.seed(42)
df['Remote %'] = np.random.randint(10, 90, size=len(df))
df['Salary (£k)'] = df['Weekly Pay (£)'] * 52 / 1000  # Convert weekly pay to annual

# 📈 Plot
plt.figure(figsize=(10, 6))
plt.scatter(df["Remote %"], df["Salary (£k)"], alpha=0.7)
plt.title("Estimated Remote Work vs. Salary by Occupation (ONS ASHE 2023)")
plt.xlabel("Remote Work (%) [Simulated]")
plt.ylabel("Salary (£k)")
plt.grid(True)
plt.tight_layout()
plt.savefig("remote_salary_live.png")
plt.show()
