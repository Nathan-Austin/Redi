"""

Imputation

https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html

fill in missing values

1. Execute the code 
   (in Jupyter, split it into multiple cells)

2. Understand what is happening
   QUESTION: What other imputation strategies exist (check out the "strategy" parameter in the documentation)?

3. Explain to the rest of the group what you did
"""

#%%
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

#%%
df = pd.DataFrame(np.random.randn(10,4), columns=list("ABCD"))
df = df.mask(np.random.random((10,4)) < 0.15)

#%% impute missing values
imputer = SimpleImputer(strategy='most_frequent')
imputer.fit(df)            # learn the most frequent value
t = imputer.transform(df)  # result is a numpy array
t
# t.shape

#%% format output as a DataFame
cols_imputed = pd.DataFrame(t, columns=df.columns)
cols_imputed.head()

