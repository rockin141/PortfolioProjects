
pip install pandas


# In[3]:


import pandas as pd


# In[4]:

#Importing file into Workspace
df = pd.read_excel('sample_superstore.xls')


# In[5]:

#overall size of the dataset (number of rows and columns),
#data types of variables, and any preliminary summary statistics (e.g., mean, median, standard deviation) to gain initial insights
df.shape
df.columns


# In[9]:
#Checking Missing Values and Data Type
df.info()


# In[10]:


# Cheking duplication 
df.duplicated().sum()





