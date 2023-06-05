#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install pandas


# In[3]:


import pandas as pd


# In[4]:


df = pd.read_excel('sample_superstore.xls')


# In[5]:


df.shape


# In[7]:


df.columns


# In[9]:


df.info()


# In[10]:


# what about duplication 
df.duplicated().sum()


# In[ ]:




