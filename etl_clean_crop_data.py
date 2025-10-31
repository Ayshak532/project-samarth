import pandas as pd
import os

# --- Step 1: Load the raw Excel ---
file_path = "data/spice_crop_data.xls"
data = pd.read_excel(file_path)

print("✅ Raw data loaded. Shape:", data.shape)

# --- Step 2: Clean column names ---
data.columns = (
    data.columns.str.strip()          # remove trailing spaces
    .str.lower()                      # make lowercase
    .str.replace(" ", "_")            # replace spaces with underscores
    .str.replace(".", "", regex=False)
)
print("\n🧹 Cleaned columns:", list(data.columns))

# --- Step 3: Handle missing values ---
missing = data.isnull().sum()
print("\n📊 Missing values per column:\n", missing)

# Fill missing numeric values with 0 (you can modify later)
for col in data.select_dtypes(include='number').columns:
    data[col] = data[col].fillna(0)

# --- Step 4: Add standard columns (optional placeholders) ---
data['state'] = "Karnataka"      # since it’s district-level spice data
data['year'] = 2021              # update if you know the dataset’s year
data['crop'] = "Spices"

# --- Step 5: Save cleaned dataset ---
os.makedirs("clean_data", exist_ok=True)
output_path = "clean_data/spice_crop_cleaned.csv"
data.to_csv(output_path, index=False)

print(f"\n✅ Cleaned dataset saved to: {output_path}")
print("\n🪄 Sample of cleaned data:\n", data.head())
