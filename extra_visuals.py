import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Data
# We skip the "Question Text" and "ImportID" rows so Q2, Q3, etc. are our headers
wsc = pd.read_csv('WSC_Data.csv', skiprows=[1, 2])

# 2. Mapping Column IDs based on your snippet:
# Q2 = First time? | Q3 = Year | Q8 = Walk-in/Appt | Q10 = Stage
# Q12_1 = Confidence Before | Q15_1 = Confidence After
col_year = 'Q3'
col_stage = 'Q10'
col_appt = 'Q8'
col_before = 'Q12_1'
col_after = 'Q15_1'

# 3. Confidence Mapping (Exactly matching your CSV strings)
likert_map = {
    'not at all confident': 1, 
    'unconfident': 2, 
    'neither confident nor unconfident': 3, 
    'confident': 4, 
    'extremely confident': 5
}

# Apply mapping (strip whitespace and lowercase for safety)
wsc['before_num'] = wsc[col_before].str.strip().str.lower().map(likert_map)
wsc['after_num'] = wsc[col_after].str.strip().str.lower().map(likert_map)

# 4. Generate Visuals
plt.style.use('ggplot') # Makes it look "Canva-ready" immediately

# VISUAL 1: Confidence Increase
avg_before = wsc['before_num'].mean()
avg_after = wsc['after_num'].mean()

plt.figure(figsize=(6, 6))
plt.bar(['Before Session', 'After Session'], [avg_before, avg_after], color=['#FF6B6B', '#4ECDC4'])
plt.ylim(1, 5)
plt.title('Average Impact on Student Confidence', fontsize=14, fontweight='bold')
plt.ylabel('Confidence Score (1-5)')
plt.savefig('confidence_jump.png', dpi=300)

# VISUAL 2: Year Breakdown (Pie Chart)
plt.figure(figsize=(7, 7))
wsc[col_year].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['#FF9F1C', '#2EC4B6', '#E71D36', '#011627'])
plt.title('Visits by Grade Level', fontweight='bold')
plt.ylabel('')
plt.savefig('year_breakdown.png', dpi=300)

# VISUAL 3: Stages (Horizontal Bar)
plt.figure(figsize=(10, 5))
wsc[col_stage].value_counts().plot(kind='barh', color='#3F51B5')
plt.title('Writing Stage at Arrival', fontweight='bold')
plt.xlabel('Number of Visits')
plt.tight_layout()
plt.savefig('writing_stages.png', dpi=300)

print("Done! check your folder for: confidence_jump.png, year_breakdown.png, and writing_stages.png")