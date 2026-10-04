import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
sp25 = pd.read_csv('WSC_Data_SP25.csv', skiprows=[1, 2])
sp26 = pd.read_csv('WSC_Data.csv', skiprows=[1, 2])

# Mapping: Q30 in SP25 [cite: 52] and Q5 in SP26  are the POE questions
def get_top_poes(df, col):
    return df[col].dropna().str.title().str.strip().value_counts().head(5)

poe_25 = get_top_poes(sp25, 'Q30')
poe_26 = get_top_poes(sp26, 'Q5')

# Create side-by-side comparison
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7), sharex=True)

poe_25.plot(kind='barh', ax=ax1, color='#457b9d')
ax1.set_title('Top Departments (Spring 2025)')
ax1.invert_yaxis()

poe_26.plot(kind='barh', ax=ax2, color='#1d3557')
ax2.set_title('Top Departments (Spring 2026)')
ax2.invert_yaxis()

plt.tight_layout()
plt.savefig('poe_shift_analysis.png')
print("POE Shift analysis saved.")