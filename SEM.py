from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('mainData.csv')

df['LowRisk'] = df['Open'] - df['Close']
df['HighRisk'] = df['High'] - df['Low']

X = df[['LowRisk', 'HighRisk']]
y = np.where(df['Close'].shift(-1) > df['Close'], 1, 0)

split_percentage = 0.8
split = int(split_percentage * len(df))

X_train = X[:split]
y_train = y[:split]

X_test = X[split:]
y_test = y[split:]

cls = SVC().fit(X_train, y_train)

df['Predicted_Signal'] = cls.predict(X)

df['Score'] = df['Close'].pct_change()
df['Score+'] = df['Score'] * df['Predicted_Signal'].shift(1)

plt.figure(figsize=(10, 6))
plt.plot(df['Score'], color='red', label='Score-')
plt.plot(df['Score+'], color='blue', label='Score+')
plt.legend()
plt.title('Score Comparison')
plt.xlabel('Time')
plt.ylabel('Score')
plt.show()


import csv

with open('results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['PatientID', 'RiskLevel']) 
    for i, risk in enumerate(df['Predicted_Signal']):
        writer.writerow([i + 1, risk]) 
print("Predictions exported to results.csv")
