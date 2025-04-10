from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# For data manipulation
import pandas as pd
import numpy as np

# To plot
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

# To ignore warnings
import warnings
warnings.filterwarnings("ignore")

# Load the dataset
df = pd.read_csv('mainData.csv')

# Feature engineering
df['LowRisk'] = df['Open'] - df['Close']
df['HighRisk'] = df['High'] - df['Low']

# Feature matrix and target variable
X = df[['LowRisk', 'HighRisk']]
y = np.where(df['Close'].shift(-1) > df['Close'], 1, 0)

# Split data into training and testing sets
split_percentage = 0.8
split = int(split_percentage * len(df))

X_train = X[:split]
y_train = y[:split]

X_test = X[split:]
y_test = y[split:]

# Train SVM classifier
cls = SVC().fit(X_train, y_train)

# Add predictions to the DataFrame
df['Predicted_Signal'] = cls.predict(X)

# Calculate scores
df['Score'] = df['Close'].pct_change()
df['Score+'] = df['Score'] * df['Predicted_Signal'].shift(1)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(df['Score'], color='red', label='Score-')
plt.plot(df['Score+'], color='blue', label='Score+')
plt.legend()
plt.title('Score Comparison')
plt.xlabel('Time')
plt.ylabel('Score')
plt.show()


import csv

# Export predictions to a CSV file
with open('results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['PatientID', 'RiskLevel'])  # Header
    for i, risk in enumerate(df['Predicted_Signal']):
        writer.writerow([i + 1, risk])  # PatientID starts from 1
print("Predictions exported to results.csv")