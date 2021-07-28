#!/usr/bin/env python
# coding: utf-8

# In[106]:


import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[81]:


tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
iris = sns.load_dataset('iris')


# In[7]:


tips.head()


# In[8]:


#dist plot


# In[20]:


sns.distplot(tips['total_bill'])


# In[12]:


#joint plot


# In[17]:


sns.jointplot(x='total_bill',y='tip',data=tips, kind='reg')


# In[18]:


#pairplots


# In[21]:


sns.pairplot(tips, hue='sex')


# In[22]:


#rugplots


# In[23]:


sns.rugplot(tips['total_bill'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[24]:


#categotical data


# In[25]:


#barplot


# In[31]:


sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)


# In[32]:


#countplot. Y axis is already defined


# In[34]:


sns.countplot(x='sex',data=tips)


# In[35]:


#box plot


# In[37]:


sns.boxplot(x='day',y='total_bill',data =tips, hue ='smoker')


# In[38]:


#violinplot


# In[41]:


sns.violinplot(x='day',y='total_bill',data=tips, hue='sex',split=True)


# In[42]:


#stripplot


# In[47]:


sns.stripplot(x='day',y='total_bill',data=tips, jitter = True)


# In[48]:


#swarmplot


# In[50]:


sns.swarmplot(x='day',y='total_bill', data = tips)


# In[51]:


#factor plots


# In[54]:


sns.factorplot(x='day',y='total_bill',data = tips, kind='bar')


# In[59]:


tips.head()


# In[60]:


flights.head()


# In[61]:


# how to heat maps


# In[63]:


tc = tips.corr()


# In[66]:


sns.heatmap(tc, annot = True, cmap = 'coolwarm')


# In[68]:


flights.head()


# In[76]:


fp = flights.pivot_table(index='month',columns='year',values='passengers')
sns.heatmap(fp, cmap = 'magma', linecolor ='white', linewidths= 2)


# In[ ]:





# In[ ]:





# In[77]:


#cluster maps


# In[78]:


sns.clustermap(fp)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[79]:


#GRIDS


# In[83]:


iris.head()


# In[92]:


g = sns.PairGrid(iris)
g.map(plt.scatter) #scatter plot
g.map_diag(sns.distplot)
g.map_lower(plt.scatter)
g.map_upper(sns.kdeplot)


# In[ ]:


#facetgrid


# In[93]:


tips.head()


# In[95]:


g = sns.FacetGrid(data=tips, col='time',row='smoker')
g.map(sns.distplot,'total_bill')


# In[ ]:





# In[ ]:





# In[96]:


#regression plots


# In[98]:


sns.lmplot(x='total_bill',y='tip',data = tips, hue='sex',)


# In[101]:


sns.lmplot(x='total_bill',y='tip',data = tips, col='sex', row ='time')


# In[104]:


sns.countplot(x='sex',data =tips)
sns.set_style('whitegrid')
sns.despine(left = True)


# In[110]:


df1 = pd.read_csv('Desktop/df1', index_col =0)


# In[111]:


df1.head()


# In[112]:


df1['A'].hist()


# In[ ]:




