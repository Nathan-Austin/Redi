"""

Binning

https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html

converts a numerical column to a matrix of binary variables

1. Execute the code 
   (in Jupyter, split it into multiple cells)

2. Understand what is happening
   QUESTION: How does changing 'n_bins' affect the model?

3. Explain to the rest of the group what you did
"""
#%%
import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer

#%%
df = pd.read_csv("penguins_simple.csv", sep =";")
df.head(2)

#%% Creating "feature matrix" (note: it's a numeric variable!)
cols = df[['Culmen Length (mm)']]
cols.head()
cols.shape

#%% transform a numerical column - strategy = "quantile"
kbins = KBinsDiscretizer(n_bins=5, encode='onehot-dense', strategy='quantile')

kbins.fit(cols)             # adjust the bin based on our data
t = kbins.transform(cols)   # transform a data in a new shape that contains the new bins
t[:5]
t.shape

#%% create a DataFrame
edges = kbins.bin_edges_[0].round(1)
edges

labels = []

for i in range(len(edges)-1):
    edge1 = edges[i]
    edge2 = edges[i+1]
    labels.append(f"{edge1}_to_{edge2}")

df_bins = pd.DataFrame(t, columns=labels)
df_bins.head()

# %%
df_bins.hist();


############ Repeat, but based on strategy = "uniform"  ############ 


#%% transform a numerical column - strategy = "uniform"

kbins = KBinsDiscretizer(n_bins=5, encode='onehot-dense', strategy='uniform')

kbins.fit(cols)             # adjust the bin based on our data
t = kbins.transform(cols)   # transform a data in a new shape that contains the new bins
t[:5]
# t.shape

#%% create a DataFrame
edges = kbins.bin_edges_[0].round(1)
edges

labels = []

for i in range(len(edges)-1):
    edge1 = edges[i]
    edge2 = edges[i+1]
    labels.append(f"{edge1}_to_{edge2}")

df_bins = pd.DataFrame(t, columns=labels)
df_bins.head()

# %%
df_bins.hist();


# %%
