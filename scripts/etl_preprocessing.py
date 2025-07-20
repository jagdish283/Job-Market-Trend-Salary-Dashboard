# scripts/etl_preprocessing.py

import pandas as pd
import os

# Load raw dataset 
raw_path = 'data/raw/ds_salaries.csv'
df = pd.read_csv(raw_path)

#Standardize column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

#Check for nulls
print("Missing values:\n", df.isnull().sum())

# Step 3: Clean/convert columns
df['salary_in_usd'] = pd.to_numeric(df['salary_in_usd'], errors='coerce')

#Create derived columns
exp_map = {
    'EN': 'Entry-level',
    'MI': 'Mid-level',
    'SE': 'Senior',
    'EX': 'Executive'
}
df['experience_label'] = df['experience_level'].map(exp_map)

# Saving processed data 
processed_path = 'data/processed/ds_salaries_clean.csv'
os.makedirs(os.path.dirname(processed_path), exist_ok=True)
df.to_csv(processed_path, index=False)

print(f"Cleaned dataset saved to: {processed_path}")
