
# coding: utf-8

# In[1]:


import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;
import seaborn as sns;
from plotnine import *;
from ggplot import *


# In[2]:


path = 'C:\\Users\\admin\\Downloads'


# In[3]:


wine_df = pd.read_csv(path + '\\winequality.csv')


# In[4]:


wine_df.head()


# In[5]:


wine_df = pd.read_csv(path + '/winequality.csv', sep=';')


# In[6]:


wine_df.head()


# In[7]:


wine_df.describe()


# In[8]:


wine_df.shape


# In[9]:


wine_df.info()


# In[10]:


wine_df.rename(columns={'fixed acidity': 'fixed_acidity',
                        'citric acid':'citric_acid',
                        'volatile acidity':'volatile_acidity',
                        'residual sugar':'residual_sugar',
                        'free sulfur dioxide':'free_sulfur_dioxide',
                        'total sulfur dioxide':'total_sulfur_dioxide'}, inplace=True)


# In[11]:


wine_df.columns


# In[12]:


wine_df.quality.unique()


# In[13]:


wine_df.quality.value_counts()


# In[14]:


pd.value_counts(wine_df.quality, sort=False).plot(kind = 'bar', rot = 0)
# plt.show()


# In[15]:


print(len(wine_df[(wine_df.quality <= 4)]))
print(len(wine_df[(wine_df.quality == 5) | (wine_df.quality == 6)]))
print(len(wine_df[(wine_df.quality >= 7)]))


# In[16]:


wine_df['quality_cat'] = pd.cut(wine_df.quality, bins=[0, 4.5, 7, 10],
                                labels=['bad', 'medium', 'good'],
                                right=False)


# In[17]:


wine_df.quality_cat.value_counts()


# In[18]:


wine_df.groupby('quality_cat').mean()


# In[19]:


box = sns.boxplot(x="quality", y='alcohol', data = wine_df)
box.set(xlabel='Wine Quality', ylabel='Alcohol %', title='Alcohol % in different wine quality types')
# plt.show()


# In[20]:


box = sns.boxplot(x="quality_cat", y='alcohol', data = wine_df)
box.set(xlabel='Wine Quality', ylabel='Alcohol %', title='Alcohol % in different wine quality types')
# plt.show()


# In[21]:


import seaborn as sns;

sp = sns.boxplot(x="quality", y="pH", data = wine_df);
sp.set(xlabel='Wine Ratings', ylabel='pH', title='pH in different types of Wine ratings')
# plt.show()


# In[22]:


vplot = sns.boxplot(x="quality", y='fixed_acidity', data = wine_df)
vplot.set(xlabel='Wine Ratings', ylabel='Fixed Acidity', title='Fixed Acidity in different types of Wine')
# plt.show()


# In[23]:


bx = sns.boxplot(x="quality", y='citric_acid', data = wine_df)
bx.set(xlabel='Wine Ratings', ylabel='Citric Acid', title='Citric acid in different types of Wine')
# plt.show()


# In[27]:


print(ggplot(wine_df, aes('alcohol', 'quality'))+geom_density()+theme(axis_text_x=element_text(angle=90, hjust=1)))
# g =  ggplot(data = wine_df +aes(x = 'alcohol', y = 'quality')+ geom_density()+ theme(axis_text_x=element_text(rotation=90, hjust=1)))
# g.draw()
