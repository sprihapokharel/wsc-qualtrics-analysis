import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Data
try:
    # Skipping metadata rows 1 and 2
    wsc = pd.read_csv('WSC_Data.csv', skiprows=[1, 2])
    wa = pd.read_csv('WA_Data.csv', skiprows=[1, 2])
    print("Files loaded successfully.")
except FileNotFoundError:
    print("Error: Ensure WSC_Data.csv and WA_Data.csv are in the folder.")
    exit()

def generate_poe_final(df, col_index, title, filename, primary_color, standout_color):
    # Select column by its position (index)
    data = df.iloc[:, col_index].dropna().astype(str).str.title().str.strip()
    
    # Get Top 10 departments
    counts = data.value_counts().head(10)
    
    if counts.empty:
        print(f"No data found for {title} at column index {col_index}")
        return

    # Assign standout color to the top bar
    colors = [standout_color] + [primary_color] * (len(counts) - 1)

    plt.figure(figsize=(10, 6))
    counts.plot(kind='barh', color=colors, edgecolor='black', alpha=0.9)
    
    # Styling
    plt.title(title, fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Number of Sessions', fontsize=12)
    plt.ylabel('Department / POE', fontsize=12)
    plt.gca().invert_yaxis()  # Highest count at the top
    plt.grid(axis='x', linestyle='--', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    print(f"Successfully saved: {filename}")

# 2. RUNNING WITH CORRECT INDICES
# WSC POE is Q5 (Index 25)
# WA POE is Q6 (Index 26)
generate_poe_final(wsc, 25, 'Top 10 Departments: Writing & Speech Center', 'wsc_poe_standout.png', '#1d3557', '#FFD700')
generate_poe_final(wa, 26, 'Top 10 Departments: Writing Associates', 'wa_poe_standout.png', '#457b9d', '#FFD700')