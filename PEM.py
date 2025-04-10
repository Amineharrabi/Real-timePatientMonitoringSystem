import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, log_loss, jaccard_score
import itertools

churn_df = pd.read_excel("mainData.xlsx", sheet_name=0)

churn_df = churn_df[['blood pressure', 'Temperature', 'Heart Rate', 'Oxygen Saturation', 'Capillary Refill Time', 'Height(FEET)', 'churn']]
churn_df['churn'] = churn_df['churn'].astype('int')

X = np.asarray(churn_df[['blood pressure', 'Temperature', 'Heart Rate', 'Oxygen Saturation', 'Capillary Refill Time', 'Height(FEET)']])
y = np.asarray(churn_df['churn'])

X = preprocessing.StandardScaler().fit(X).transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)

LR = LogisticRegression(C=0.01, solver='liblinear').fit(X_train, y_train)

yhat = LR.predict(X_test)
yhat_prob = LR.predict_proba(X_test)

print("Jaccard Score:", jaccard_score(y_test, yhat, pos_label=0))
print("Log Loss:", log_loss(y_test, yhat_prob))
print("Classification Report:\n", classification_report(y_test, yhat))

def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

cnf_matrix = confusion_matrix(y_test, yhat, labels=[1, 0])
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=['churn=1', 'churn=0'], normalize=False, title='Confusion matrix')
plt.show()
import csv

with open('results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['PatientID', 'RiskLevel'])  
    for i, risk in enumerate(yhat):
        writer.writerow([i + 1, risk])  
print("Predictions exported to results.csv")
