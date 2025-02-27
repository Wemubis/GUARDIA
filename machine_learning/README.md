# MachineLearning_P5

## Dataset Information

- **Columns:**
  - `step`: Time of the transaction within a month.
  - `type`: Type of transaction (e.g., 'TRANSFER', 'CASH_OUT').
  - `amount`: Transaction amount.
  - `oldbalanceOrg`: Original balance in the source account.
  - `newbalanceOrig`: New balance in the source account.
  - `oldbalanceDest`: Original balance in the destination account.
  - `newbalanceDest`: New balance in the destination account.
  - `isFraud`: Binary label indicating if the transaction is fraudulent (1) or not (0).
  - `isFlaggedFraud`: Binary flag indicating if the transaction is flagged as fraudulent (1) or not (0).

<br><br>

## Repository Content

### 1. Dataset Exploration

- Displaying basic information about the dataset with `df.info()`:

    ```python
    print(df.info())
    ```

- Showing summary statistics for numerical columns with `df.describe()`:

    ```python
    print(df.describe())
    ```

- Displaying the first few rows of the dataset with `df.head()`:

    ```python
    print(df.head())
    ```

<br>

### 2. Analysis of the 'isFraud' Column

- Exploring the 'isFraud' column to understand the distribution of fraudulent and non-fraudulent transactions:

    ```python
    # Display unique values in the 'isFraud' column
    print(df['isFraud'].unique())

    # Display distribution of values in the 'isFraud' column
    print(df['isFraud'].value_counts())

    # Display percentage of fraudulent/non-fraudulent transactions
    print(df['isFraud'].value_counts(normalize=True) * 100)

    # Display missing values in the dataset
    print(df.isnull().sum())
    ```

<br>

### 3. In-depth Data Analysis

- Conducting detailed analysis on some features:

  - Transaction Types: Analyzing the distribution of transaction types for fraudulent transactions:

    ```python
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=(12, 6))
    sns.countplot(x='type', data=df[df['isFraud'] == 1])
    plt.title('Distribution of Transaction Types for Fraudulent Transactions')
    plt.xlabel('Transaction Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()
    ```

  - Amount Analysis: Exploring the distribution of transaction amounts for fraudulent transactions:

    ```python
    plt.figure(figsize=(12, 6))
    sns.histplot(df[df['isFraud'] == 1]['amount'], bins=30, kde=True)
    plt.title('Distribution of Transaction Amounts for Fraudulent Transactions')
    plt.xlabel('Transaction Amount')
    plt.ylabel('Count')
    plt.show()
    ```

  - Boxplot of Transaction Amounts by Fraud Status:

    ```python
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='isFraud', y='amount', data=df)
    plt.title('Box Plot of Transaction Amounts by Fraud Status')
    plt.xlabel('isFraud')
    plt.ylabel('Amount')
    plt.show()
    ```

  - Bar Chart of Fraudulent vs Non-Fraudulent Transaction Percentages:

    ```python
    plt.figure(figsize=(8, 6))
    fraud_percentage.plot(kind='bar', color=['green', 'red'])
    plt.title('Percentage of Fraud/Non-Fraud Transactions')
    plt.xlabel('isFraud')
    plt.ylabel('Percentage')
    plt.xticks(rotation=0)
    plt.show()
    ```

  - Correlation Matrix:

    ```python
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()
    ```

<br>

### General Overview:
  
- 'TRANSFER' and 'CASH_OUT' transactions dominate fraud cases, confirming their predominant role in these incidents.

- The analysis of both source and destination balances reveals various patterns for fraud, highlighting the potential usefulness of this information.

- No clear temporal trend emerges in fraud, but time-related features warrant further exploration.

- Flagged transactions remain infrequent in fraud cases, suggesting gaps in the reporting process.

- The significant imbalance between fraudulent and non-fraudulent transactions (99.87% vs 0.13%) highlights the challenge of class imbalance when training models.
