import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Data
wsc = pd.read_csv('WSC_Data.csv', skiprows=[1, 2])
wa = pd.read_csv('WA_Data.csv', skiprows=[1, 2])

def calculate_confidence_delta(df, before_col, after_col):
    # Map text responses to numbers (1-5)
    mapping = {
        'Not at all confident': 1, 'Unconfident': 2, 
        'Neither confident nor unconfident': 3, 
        'Confident': 4, 'Extremely confident': 5
    }
    
    # Apply mapping and drop rows with missing data
    before = df[before_col].map(mapping).dropna()
    after = df[after_col].map(mapping).dropna()
    
    # Calculate averages
    avg_before = before.mean()
    avg_after = after.mean()
    delta = avg_after - avg_before
    
    return avg_before, avg_after, delta

# 2. Map Columns based on CSV headers
# WSC: Q12_1 is Before, Q15_1 is After
wsc_before, wsc_after, wsc_delta = calculate_confidence_delta(wsc, 'Q12_1', 'Q15_1')

# WA: Q12_1 is Before, Q15_1 is After
wa_before, wa_after, wa_delta = calculate_confidence_delta(wa, 'Q12_1', 'Q15_1')

# 3. Create Visualization
labels = ['WSC Program', 'WA Program']
before_scores = [wsc_before, wa_before]
after_scores = [wsc_after, wa_after]

x = range(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar([p - width/2 for p in x], before_scores, width, label='Before Session', color='#8d99ae')
rects2 = ax.bar([p + width/2 for p in x], after_scores, width, label='After Session', color='#1d3557')

# Add labels and formatting
ax.set_ylabel('Average Confidence Score (1-5)')
ax.set_title('Impact on Student Confidence: Before vs. After', fontweight='bold', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylim(1, 5) # Scale reflects the 1-5 Likert options
ax.legend()

# Add text for the "Delta" on top of the bars
ax.text(0, wsc_after + 0.1, f"+{wsc_delta:.2f} Boost", ha='center', fontweight='bold', color='#e63946')
ax.text(1, wa_after + 0.1, f"+{wa_delta:.2f} Boost", ha='center', fontweight='bold', color='#e63946')

plt.tight_layout()
plt.savefig('confidence_boost_comparison.png')
print(f"WSC Boost: {wsc_delta:.2f} | WA Boost: {wa_delta:.2f}")