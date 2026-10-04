import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Data
try:
    wsc = pd.read_csv('WSC_Data.csv', skiprows=[1, 2])
    wa = pd.read_csv('WA_Data.csv', skiprows=[1, 2])
    print("Files loaded successfully.")
except FileNotFoundError:
    print("Error: Ensure WSC_Data.csv and WA_Data.csv are in the folder.")
    exit()

def generate_unique_poe_chart(df, name_idx, poe_idx, title, filename, primary_color, standout_color):
    # Create a temporary dataframe with just Name and POE
    # Index 21 is Name (Q1) for both WSC and WA based on your CSV
    temp_df = df.iloc[:, [name_idx, poe_idx]].copy()
    temp_df.columns = ['Name', 'POE']
    
    # Standardize data
    temp_df['Name'] = temp_df['Name'].astype(str).str.lower().str.strip()
    temp_df['POE'] = temp_df['POE'].dropna().astype(str).str.title().str.strip()
    
    # DROP DUPLICATES: This ensures each name only appears once
    unique_visitors = temp_df.drop_duplicates(subset=['Name'])
    
    # Count the unique POEs
    counts = unique_visitors['POE'].value_counts().head(10)
    
    if counts.empty:
        print(f"No unique data found for {title}")
        return

    # Assign standout color to the top bar
    colors = [standout_color] + [primary_color] * (len(counts) - 1)

    plt.figure(figsize=(10, 6))
    counts.plot(kind='barh', color=colors, edgecolor='black', alpha=0.9)
    
    plt.title(title + " (Unique Students)", fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Number of Unique Students')
    plt.ylabel('Department / POE')
    plt.gca().invert_yaxis()
    plt.grid(axis='x', linestyle='--', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    print(f"Saved Unique Chart: {filename}")

# 2. EXECUTE
# Name is Index 21 (Q1) for both 
# WSC POE is Index 25 (Q5)
# WA POE is Index 26 (Q6)
generate_unique_poe_chart(wsc, 21, 25, 'Top 10 Departments: WSC', 'wsc_unique_poe.png', '#1d3557', '#FFD700')
generate_unique_poe_chart(wa, 21, 26, 'Top 10 Departments: WA', 'wa_unique_poe.png', '#457b9d', '#FFD700')