import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming your dataset is in a CSV file named 'financial_data.csv'
file_path = r'\Users\mewen\ML_P5\clean_fraud.csv'

# Load the dataset into a pandas DataFrame
df = pd.read_csv(file_path)



##### CHECK IF LOADED WELL #####
# Display basic information about the dataset
print("Dataset Overview:")
print(df.info())

# Display summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Display the first few rows of the dataset
print("\nFirst Few Rows:")
print(df.head())



##### WHAT ABOUT 'isFraud' #####
# Display unique values in the 'isFraud' column
print("\nUnique values in 'isFraud' column:")
print(df['isFraud'].unique())

# Display the distribution of values in the 'isFraud' column
print("\nValue Counts in 'isFraud' column:")
print(df['isFraud'].value_counts())

# Display percentage of fraud/non-fraud transactions
fraud_percentage = df['isFraud'].value_counts(normalize=True) * 100
print("\nPercentage of Fraud/Non-Fraud Transactions:")
print(fraud_percentage)

# Display any missing values in the dataset
print("\nMissing Values:")
print(df.isnull().sum())



# ##### WHAT ABOUT GRAPHS #####
# # replacing string to integer values bassed the max occurance in the data
# df.replace(to_replace = ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'], value = [4,5,2,3,1],inplace = True)

# # Transaction Types: Analyzed the distribution of transaction types for fraudulent transactions
# plt.figure(figsize=(12, 6))
# sns.countplot(x='type', data=df[df['isFraud'] == 1])
# plt.title('Distribution of Transaction Types for Fraudulent Transactions')
# plt.xlabel('Transaction Type')
# plt.ylabel('Count')
# plt.xticks(rotation=45)
# plt.show()

# # Amount Analysis: Explored the distribution of transaction amounts for fraudulent transactions
# plt.figure(figsize=(12, 6))
# sns.histplot(df[df['isFraud'] == 1]['amount'], bins=30, kde=True)
# plt.title('Distribution of Transaction Amounts for Fraudulent Transactions')
# plt.xlabel('Transaction Amount')
# plt.ylabel('Count')
# plt.show()

# # To visualize the summary of the distribution of a numerical variable, identify outliers, and compare distributions.
# plt.figure(figsize=(10, 6))
# sns.boxplot(x='isFraud', y='amount', data=df)
# plt.title('Box Plot of Transaction Amounts by Fraud Status')
# plt.xlabel('isFraud')
# plt.ylabel('Amount')
# plt.show()

# # Visualize the percentage of fraud/non-fraud transactions
# plt.figure(figsize=(8, 6))
# fraud_percentage.plot(kind='bar', color=['green', 'red'])
# plt.title('Percentage of Fraud/Non-Fraud Transactions')
# plt.xlabel('isFraud')
# plt.ylabel('Percentage')
# plt.xticks(rotation=0)
# plt.show()

# # Visualize the correlation matrix
# plt.figure(figsize=(10, 8))
# sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
# plt.title('Correlation Matrix')
# plt.show()
