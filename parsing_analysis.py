import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data
wsc = pd.read_csv('WSC_Data.csv', skiprows=[1, 2])

# 2. Broad Speech Keywords
speech_keywords = ['speech', 'presentation', 'oral', 'talk', 'speak', 'pitch', 'powerpoint', 'slide', 'comm', 'public']

# 3. Simple Search Logic
def is_speech(text):
    if pd.isna(text):
        return 'Writing & General'
    text = str(text).lower()
    if any(k in text for k in speech_keywords):
        return 'Speech & Presentation'
    else:
        return 'Writing & General'

wsc['Speech_Status'] = wsc['Q9'].apply(is_speech)
counts = wsc['Speech_Status'].value_counts()

# 4. Bulletproof Visualization
plt.figure(figsize=(8, 8))

# Define a color map that works regardless of how many categories are found
color_map = {'Writing & General': '#1d3557', 'Speech & Presentation': '#ffb703'}
current_colors = [color_map.get(label, '#8d99ae') for label in counts.index]

# Removed 'explode' to prevent the length error
plt.pie(counts, labels=counts.index, autopct='%1.1f%%', 
        startangle=140, colors=current_colors, shadow=False)

plt.title('Center Usage: Speech vs. General Support', fontsize=14, fontweight='bold')
plt.savefig('speech_impact.png', dpi=300)

print("--- DATA FOR YOUR KAHOOT ---")
print(counts)