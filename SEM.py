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
pd.read_csv("mainData.csv",5,6,7,8,9,10)

df = pd.read_csv('mainData.csv') 
df

df['LowRisk'] = df.Open - df.Close 
df['HighRisk'] = df.High - df.Low 
  
X = df[['LowRisk', 'HighRisk']] 
X.head() 
y = np.where(df['Close'].shift(-1) > df['Close'], 1, 0) 
y

split_percentage = 0.8
split = int(split_percentage*len(df)) 
  
X_train = X[:split] 
y_train = y[:split] 
  
X_test = X[split:] 
y_test = y[split:]

cls = SVC().fit(X_train, y_train)

df['Predicted_Signal'] = cls.predict(X)

df['Score-'] = df.Close.pct_change()
df['Score+'] = df.Score *df.Predicted_Signal.shift(1)

import matplotlib.pyplot as plt 
#%matplotlib inline 
  
plt.plot(Df['Score-'],color='red') 
plt.plot(Df['Score+'],color='blue')


