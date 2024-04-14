"""

Scaling

https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html

converts a numerical column to a scaled/normalized numerical column

1. Execute the code 
   (in Jupyter, split it into multiple cells)

2. Understand what is happening
   QUESTION: Research the pros/cons of scaling a numerical variable.

3. Explain to the rest of the group what you did
"""
#%%
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

#%%
df = pd.read_csv("penguins_simple.csv", sep =";")

#%% Creating "feature matrix"
cols = df[["Culmen Length (mm)"]]
cols.head()
cols.shape

#%% transform a numerical column
scaler = MinMaxScaler()
scaler.fit(cols)               # learn the min and max of the data
t = scaler.transform(cols)     # apply the transformation to the data
t[:5]
t.shape

#%% format output as a DataFame
cols_scaled = pd.DataFrame(t, columns=cols.columns)
cols_scaled.head()



# %%
