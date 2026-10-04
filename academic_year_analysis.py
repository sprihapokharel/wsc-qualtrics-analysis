import pandas as pd
import matplotlib.pyplot as plt

# Load Fall 25 and Spring 26 data
fa25 = pd.read_csv('WSC_Data_FA25.csv', skiprows=[1, 2])
sp26 = pd.read_csv('WSC_Data.csv', skiprows=[1, 2])

# Combine them into one full-year dataset
full_year = pd.concat([fa25, sp26])
# Clean the date column [cite: 8, 68]
full_year['Date'] = pd.to_datetime(full_year['RecordedDate'], errors='coerce')
year_trend = full_year.groupby(full_year['Date'].dt.to_period('W').dt.to_timestamp()).size()

plt.figure(figsize=(15, 6))
# Create a filled area chart for visual impact
plt.fill_between(year_trend.index, year_trend.values, color='#457b9d', alpha=0.3)
plt.plot(year_trend.index, year_trend.values, color='#1d3557', linewidth=2)

plt.title('2025-2026 Academic Year Engagement Trend', fontsize=16, fontweight='bold')
plt.ylabel('Number of Sessions')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('academic_year_trend.png')

print(f"Total Academic Year Visits: {len(full_year)}")
print("Academic year chart saved as 'academic_year_trend.png'")