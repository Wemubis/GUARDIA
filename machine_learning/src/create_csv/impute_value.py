import pandas as pd
import numpy as np

# Assuming your dataset is in a CSV file named 'financial_data.csv'
input_file = r'\Users\mewen\ML_P5\clean_fraud.csv'
output_file = r"\Users\mewen\ML_P5\imputed_fraud.csv"

# Load the dataset into a pandas DataFrame
df = pd.read_csv(input_file)

# Select a subset of data to impute missing values (e.g., 5% of values)
missing_indices = np.random.choice(df.index, size=int(0.05 * len(df)), replace=False)

# Impute missing values by replacing with NaN
df.loc[missing_indices, 'amount'] = np.nan

# Imputation of missing value based on mean
df['amount'] = df['amount'].fillna(df['amount'].mean())

# Save the updated DataFrame to a new CSV file
df.to_csv(output_file, index=False)
