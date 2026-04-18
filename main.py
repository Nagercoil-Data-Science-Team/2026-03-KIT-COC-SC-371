import pandas as pd

# Load Excel file
df = pd.read_excel("data.xlsx")

# First 5 rows check
print(df.head())

# Column names check
print(df.columns)


# ==========================================
# 🔹 STEP 3: FILTER DATA (Important for Research)
# ==========================================

# 1. Filter Year (2000–2025)
df = df[df['YEAR OF INITIATION'] >= 2000]
df = df[df['YEAR OF INITIATION'] <= 2025]

# 2. Filter only decided cases (remove Pending)
df = df[df['STATUS/OUTCOME OF ORIGINAL PROCEEDINGS'] != 'Pending']

# 3. Filter sectors (Energy / Environment / Infrastructure)
sector_keywords = ['Energy', 'Environment', 'Construction', 'Infrastructure', 'Transport']

df = df[df['ECONOMIC SECTOR'].str.contains('|'.join(sector_keywords), case=False, na=False)]


# ==========================================
# 💾 SAVE FINAL DATASET TO EXCEL
# ==========================================

df.to_excel("filtered_isds_dataset.xlsx", index=False)


# ==========================================
# Final dataset ready for analysis
# ==========================================

print("Filtered Data Shape:", df.shape)
print(df.head())
print("✅ File saved as: filtered_isds_dataset.xlsx")