import pandas as pd

# Assuming your dataset is in a CSV file named 'financial_data.csv'
input_file = r'\Users\mewen\ML_P5\clean_fraud.csv'
output_file = r"\Users\mewen\ML_P5\clean_fraud_without_outliers.csv"

# Load the dataset into a pandas DataFrame
df = pd.read_csv(input_file)

# Outlier detection using threshold method
lower_threshold = df['amount'].quantile(0.05)
upper_threshold = df['amount'].quantile(0.95)

# Replace outliers with NaN
df.loc[(df['amount'] < lower_threshold) | (df['amount'] > upper_threshold), 'amount'] = np.nan

# Impute NaN values using mean
df['amount'] = df['amount'].fillna(df['amount'].mean())

# Save the DataFrame without outliers to a new CSV file
df.to_csv(output_file, index=False)
