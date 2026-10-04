import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data, skipping the 2 extra metadata rows Qualtrics exports
# This ensures 'RecordedDate' is seen as the header
try:
    wsc = pd.read_csv('WSC_Data.csv', skiprows=[1, 2])
    wa = pd.read_csv('WA_Data.csv', skiprows=[1, 2])
    print("Files loaded successfully.")
except FileNotFoundError:
    print("Error: Ensure WSC_Data.csv and WA_Data.csv are in the same folder as this script.")
    exit()

# 2. Clean and Convert Dates
# Using errors='coerce' turns unparseable strings into NaT (Not a Time)
wsc['Date'] = pd.to_datetime(wsc['RecordedDate'], errors='coerce')
wa['Date'] = pd.to_datetime(wa['RecordedDate'], errors='coerce')

# Drop rows where dates couldn't be parsed
wsc = wsc.dropna(subset=['Date'])
wa = wa.dropna(subset=['Date'])

# 3. Group by Week
# This rounds every date to the start of its week so we can count them
wsc_trend = wsc.groupby(wsc['Date'].dt.to_period('W').dt.to_timestamp()).size()
wa_trend = wa.groupby(wa['Date'].dt.to_period('W').dt.to_timestamp()).size()

# 4. Create the Visualization
plt.figure(figsize=(12, 6))

# Plotting WSC
plt.plot(wsc_trend.index, wsc_trend.values, 
         label='WSC Visits', color='#0077b6', linewidth=3, marker='o', markersize=8)

# Plotting WA
plt.plot(wa_trend.index, wa_trend.values, 
         label='WA Meetings', color='#e63946', linewidth=3, marker='s', markersize=8)

# 5. Professional Styling
plt.title('Spring 2026 Engagement Trends: WSC vs. Writing Associates', fontsize=16, pad=20, fontweight='bold')
plt.xlabel('Semester Timeline (Weeks)', fontsize=12)
plt.ylabel('Number of Sessions', fontsize=12)

# Add a light grid for readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Remove the top and right spines for a modern, clean "Canva-ready" look
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Add Legend
plt.legend(frameon=False, fontsize=11)

# 6. Save and Finish
plt.tight_layout()
plt.savefig('combined_trend.png', dpi=300)
print("Success! Your chart has been saved as 'combined_trend.png'.")

