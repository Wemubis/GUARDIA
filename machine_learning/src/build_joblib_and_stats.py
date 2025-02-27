import sys
import numpy as np
import pandas as pd
import xgboost as xgb
import lightgbm as lgb
from joblib import dump
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from sklearn.mixture import GaussianMixture
from mlxtend.frequent_patterns import apriori
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from mlxtend.preprocessing import TransactionEncoder
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression, LinearRegression, RidgeClassifier, Lasso
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, silhouette_score


#################### METHOD ####################
def choose_method():
	while True:
		# Display available algorithms
		print("Available algorithms:")
		print("- 'linear_regression'")
		print("- 'logistic_regression'")
		print("- 'ridge_regression'")
		print("- 'lasso_regression'")
		print("- 'decision_tree'")
		print("- 'random_forest'")
		print("- 'gradient_boosting'")
		print("- 'xgboost'")
		print("- 'lightgbm'")
		print("- 'kmeans'")
		print("- 'hierarchical_clustering'")
		print("- 'gaussian_mixture_models'")
		print("- 'apriori'")
		print("- 'exit' to quit")

		algorithm = input("Enter the desired algorithm: ").lower()

		if algorithm == 'exit':
			sys.exit(0)

		if algorithm in ['random_forest', 'decision_tree', 'linear_regression', 'logistic_regression',
							'ridge_regression', 'lasso_regression', 'gradient_boosting', 'xgboost', 'apriori',
							'lightgbm', 'kmeans', 'hierarchical_clustering', 'gaussian_mixture_models']:
			break

		else:
			print(f"\nInvalid algorithm choice: {algorithm}. Please choose a valid algorithm or type 'exit' to quit.\n")

	return algorithm


#################### INIT ####################
def init_model(algorithm):
	elif algorithm == 'linear_regression':
		model = LinearRegression()
	elif algorithm == 'logistic_regression':
		model = LogisticRegression(random_state=42)
	elif algorithm == 'ridge_regression':
		model = RidgeClassifier(random_state=42)
	elif algorithm == 'lasso_regression':
		model = Lasso(random_state=42)
	elif algorithm == 'decision_tree':
		model = DecisionTreeClassifier(random_state=42)
	if algorithm == 'random_forest':
		model = RandomForestClassifier(n_estimators=100, random_state=42)
	elif algorithm == 'gradient_boosting':
		model = GradientBoostingClassifier(random_state=42)
	elif algorithm == 'xgboost':
		model = xgb.XGBClassifier(random_state=42)
	elif algorithm == 'lightgbm':
		model = lgb.LGBMClassifier(random_state=42)
	elif algorithm == 'kmeans':
		model = KMeans(n_clusters=2, random_state=42)
	elif algorithm == 'hierarchical_clustering':
		model = AgglomerativeClustering(n_clusters=2, linkage='average')
	elif algorithm == 'gaussian_mixture_models':
		model = GaussianMixture(n_components=2, random_state=42)
	elif algorithm == 'apriori':
		model = 'apriori'

	return model



#################### EVALUATE CLUSTERING ####################
def evaluate_clustering(X, labels, algorithm):
	if algorithm == 'kmeans':
		silhouette = silhouette_score(X, labels)
		inertia = np.sum(np.min(cdist(X, labels.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0]
		return silhouette, inertia	
	elif algorithm == 'hierarchical_clustering':
		silhouette = silhouette_score(X, labels)
		return silhouette
	else:
		return None


#################### EVALUATE ####################
def train_and_evaluate():
	# Read the dataset
	file_path = r'\Users\mewen\ML_P5\clean_fraud.csv'
	df = pd.read_csv(file_path)

	# Mapping transaction types to numerical values
	df.replace(to_replace=['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'], value=[4, 5, 2, 3, 1], inplace=True)

	# Split features and target variable
	X = df.drop('isFraud', axis=1)
	y = df['isFraud']

	# Split the data into training and testing sets | 80% of data for training and 20% for testing
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

	# Algorithm choice
	algorithm = choose_method()

	# Initialize the classifier based on user input
	model = init_model(algorithm)
	
	algorithmJoblib = r"joblib\\" + algorithm + r".joblib"

	# Train the model or fit the clustering algorithm
	if algorithm in ['kmeans', 'gaussian_mixture_models', 'hierarchical_clustering']:
		labels = model.fit_predict(X)
		dump(labels, algorithmJoblib)
	elif algorithm != 'apriori':
		model.fit(X_train, y_train)
		dump(model, algorithmJoblib)


	# Evaluate the model or clustering algorithm
	if algorithm not in ['kmeans', 'hierarchical_clustering', 'gaussian_mixture_models', 'apriori']:
		predictions = model.predict(X_test)
		predictions = (predictions > 0.5).astype(int)
		accuracy = accuracy_score(y_test, predictions)
		conf_matrix = confusion_matrix(y_test, predictions)
		classification_rep = classification_report(y_test, predictions)

		# Display results
		print("Classification Algorithm Results:")
		print(f"Algorithm: {algorithm}")
		print(f"Accuracy: {accuracy}")
		print(f"Confusion Matrix:\n{conf_matrix}")
		print(f"Classification Report:\n{classification_rep}")

	 # Apply Apriori algorithm
	elif algorithm == 'apriori':
		# Assuming df is your DataFrame and 'type' is the column with transaction data
		transactions = df['type'].apply(lambda x: [str(x)]).tolist()

		# Transform the dataset into a one-hot encoded format
		te = TransactionEncoder()
		te_ary = te.fit(transactions).transform(transactions)
		df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

		# Apply Apriori algorithm to find frequent itemsets
		frequent_itemsets = apriori(df_encoded, min_support=0.2, use_colnames=True)

		# Display the frequent itemsets
		print("Frequent Itemsets:")
		print(frequent_itemsets)

	else:
		# Evaluate clustering
		clustering_metrics = evaluate_clustering(X, labels, algorithm)

		# Display clustering results
		if algorithm in ['kmeans', 'hierarchical_clustering']:
			print("\nClustering Algorithm Results:")
			print(f"Algorithm: {algorithm}")
			print(f"Silhouette Score: {clustering_metrics[0]}")
			if algorithm == 'kmeans':
				print(f"Inertia (Sum of Squared Distances): {clustering_metrics[1]}")


#################### MAIN ####################
if __name__ == "__main__":
	if len(sys.argv) != 1:
		print("Usage: python script.py")
		sys.exit(1)

	train_and_evaluate()
