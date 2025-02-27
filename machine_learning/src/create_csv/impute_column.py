import csv

input_file = r"\Users\mewen\ML_P5\dataset_fraud.csv"
# output_file = r"\Users\mewen\ML_P5\clean_fraud.csv"
output_file = r"\Users\mewen\ML_P5\clean_fraud_2.csv"

# Columns to keep
# columns_to_keep = ['step', 'type', 'amount','oldbalanceOrg','newbalanceOrig','oldbalanceDest','newbalanceDest','isFraud','isFlaggedFraud']
columns_to_keep = ['step', 'type', 'amount','isFraud','isFlaggedFraud']

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    headers = reader.fieldnames

    # Filter columns to keep
    new_headers = [header for header in headers if header in columns_to_keep]

    writer = csv.DictWriter(outfile, fieldnames=new_headers)
    writer.writeheader()

    for row in reader:
        # Write rows with selected columns
        writer.writerow({col: row[col] for col in new_headers})