
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import pandas as pd
re11 = pd.read_excel("LL1.xlsx")
re21 = pd.read_excel("MI1.xlsx")
re31 = pd.read_excel("DC1.xlsx")
re41 = pd.read_excel("T1.xlsx")

re = pd.merge(re11, re31, how = 'outer')
ret = pd.merge(re21, re41, how = 'outer')
re = pd.merge(re, ret, how = 'outer')
writer = pd.ExcelWriter('outputRE.xlsx')
re.to_excel(writer, sheet_name='Sheet1')
writer.save()


# In[6]:


import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#we read the table and create correlation matrix
re = pd.read_excel("outputRE.xlsx")
corr_s = re.corr(method = 'spearman')
corr_k = re.corr(method = 'kendall')
print('Spearman')
print(corr_s)
#we save the matrix into file
writer = pd.ExcelWriter('outputCORRD.xlsx')
corr_s.to_excel(writer, sheet_name='Spearman')
corr_k.to_excel(writer, sheet_name='Kendall')
writer.save()

#we build a plot using matplotlib ( google for matshow)
fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111)
cax_s = ax1.matshow(corr_s, interpolation='nearest')
fig1.colorbar(cax_s)

#we add labels and print
alpha = ['LL', 'Dice', 'MI', 'T score']
ax1.set_xticklabels(['']+alpha)
ax1.set_yticklabels(['']+alpha)
plt.show()

print('Kendall')
print(corr_k)

#same for the second plot
fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111)
cax_k = ax2.matshow(corr_k, interpolation='nearest')
fig2.colorbar(cax_k)
alpha = ['LL', 'Dice', 'MI', 'T score']
ax2.set_xticklabels(['']+alpha)
ax2.set_yticklabels(['']+alpha)
plt.show()


# In[2]:


import matplotlib
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

from pandas import DataFrame, read_csv
f = 'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'
df = read_csv(f)
df=df[0:10]
df
re = pd.read_excel("outputRE.xlsx")

