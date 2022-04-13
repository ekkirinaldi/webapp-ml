import pandas as pd
from sklearn import linear_model
import pickle 

df = pd.read_csv('deploy-lr-project/ml-model/prices.csv')
print(df)

y=df['Value']
X=df[['Rooms','Distance']]

#%%
lm=linear_model.LinearRegression()
lm.fit(X,y)

pickle.dump(lm, open('model.pkl','wb'))
