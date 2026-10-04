import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
sp25 = pd.read_csv('WSC_Data_SP25.csv', skiprows=[1, 2])
sp26 = pd.read_csv('WSC_Data.csv', skiprows=[1, 2])

def get_retention_data(df, col_name):
    # Standardize responses to 'Yes' or 'No'
    data = df[col_name].dropna().str.strip().str.capitalize()
    return data.value_counts(normalize=True) * 100

# Mapping: Q4 in SP25 [cite: 25] and Q3 in SP26  are the "First Time" questions
retention_25 = get_retention_data(sp25, 'Q4')
retention_26 = get_retention_data(sp26, 'Q3')

# Plotting
labels = ['Returning (No)', 'First-Time (Yes)']
val_25 = [retention_25.get('No', 0), retention_25.get('Yes', 0)]
val_26 = [retention_26.get('No', 0), retention_26.get('Yes', 0)]

x = range(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar([p - width/2 for p in x], val_25, width, label='Spring 2025', color='#8d99ae')
ax.bar([p + width/2 for p in x], val_26, width, label='Spring 2026', color='#1d3557')

ax.set_ylabel('Percentage of Total Visits (%)')
ax.set_title('Retention Growth: First-Time vs. Returning Visitors', fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.tight_layout()
plt.savefig('retention_comparison.png')
print("Retention chart saved.")