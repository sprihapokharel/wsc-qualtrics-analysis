import pandas as pd
import matplotlib.pyplot as plt

def get_weekly_trend(file_path):
    # Load data skipping the 2 metadata rows common in Qualtrics [cite: 1, 65]
    df = pd.read_csv(file_path, skiprows=[1, 2])
    # Convert RecordedDate to datetime objects [cite: 8, 68]
    df['Date'] = pd.to_datetime(df['RecordedDate'], errors='coerce')
    df = df.dropna(subset=['Date'])
    # Group by week and count visits
    return df.groupby(df['Date'].dt.to_period('W').dt.to_timestamp()).size()

# Load both years
sp25_trend = get_weekly_trend('WSC_Data_SP25.csv')
sp26_trend = get_weekly_trend('WSC_Data.csv')

plt.figure(figsize=(12, 6))
# Plot Spring 25 as a baseline (dashed) and Spring 26 as a solid line
plt.plot(sp25_trend.index.strftime('%b %d'), sp25_trend.values, label='Spring 2025', color='grey', linestyle='--')
plt.plot(sp26_trend.index.strftime('%b %d'), sp26_trend.values, label='Spring 2026', color='#1d3557', linewidth=3)

plt.title('Growth Comparison: Spring 2025 vs. Spring 2026', fontsize=14, fontweight='bold')
plt.ylabel('Total Weekly Visits')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('spring_comparison.png')
print("Spring comparison chart saved as 'spring_comparison.png'")