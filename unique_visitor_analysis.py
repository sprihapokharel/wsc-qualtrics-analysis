import pandas as pd

# Load the datasets, skipping the two extra metadata rows from Qualtrics
df_fa25 = pd.read_csv('WSC_Data_FA25.csv', skiprows=[1, 2])
df_sp26 = pd.read_csv('WSC_Data.csv', skiprows=[1, 2])

def get_clean_unique_names(df, column_name):
    # 1. Select the name column
    # 2. Drop empty responses
    # 3. Strip whitespace and standardize to Title Case for comparison
    names = df[column_name].dropna().str.strip().str.title()
    return set(names)

# Get unique names for each semester
names_fa25 = get_clean_unique_names(df_fa25, 'Q1')
names_sp26 = get_clean_unique_names(df_sp26, 'Q1')

# Calculate the total unique reach for the whole year
all_unique_names = names_fa25.union(names_sp26)

print(f"Unique Visitors Fall 2025: {len(names_fa25)}")
print(f"Unique Visitors Spring 2026: {len(names_sp26)}")
print(f"Total Unique Visitors for the Academic Year: {len(all_unique_names)}")