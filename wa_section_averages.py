import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Data
wa = pd.read_csv('WA_Data.csv', skiprows=[1, 2])

# 2. List of just the section numbers you provided
section_numbers = [
    '01', '03', '04', '05', '06', '08', '09', '10', 
    '11', '12', '14', '15', '18', '19', '20', '22', '23', '24'
]

# 3. Fuzzy Cleaning Logic
def fuzzy_clean(text):
    if pd.isna(text): return None
    text = str(text).replace(" ", "")
    
    # Check if it's FYC first
    if 'FYC' in text.upper():
        return 'FYC-101'
    
    # If it's an FYS, find which number matches
    if 'FYS' in text.upper() or '102' in text:
        for num in section_numbers:
            if f"-{num}" in text or f"102{num}" in text or text.endswith(num):
                return f"FYS-102-{num}"
    
    return None # Ignore everything else

# Apply to Q6 (Index 27) [cite: 98]
wa['Clean_Section'] = wa.iloc[:, 27].apply(fuzzy_clean)

# 4. Filter to only our matched sections
fys_only = wa.dropna(subset=['Clean_Section'])
counts = fys_only['Clean_Section'].value_counts()

if counts.empty:
    print("Still no matches. Let's try printing unique values to see what students typed:")
    print(wa.iloc[:, 27].unique()[:10])
    exit()

# 5. Calculate Stats
avg_v = counts.mean()
med_v = counts.median()

print(f"Sections Found: {len(counts)}")
print(f"Average: {avg_v:.2f} | Median: {med_v:.2f}")

# 6. Visualization
plt.figure(figsize=(12, 6))
counts.plot(kind='bar', color='#457b9d', edgecolor='black')
plt.axhline(y=avg_v, color='red', linestyle='--', label=f'Avg: {avg_v:.1f}')
plt.title('Writing Associate Visits by FYS Section', fontweight='bold')
plt.ylabel('Number of Visits')
plt.legend()
plt.tight_layout()
plt.savefig('wa_fys_fixed.png', dpi=300)