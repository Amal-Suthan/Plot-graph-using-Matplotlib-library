#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


file_name = "Desktop/car_financing.csv"
df = pd.read_csv(file_name)


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


month = df.loc[:, 'Month'].values
interestpaid = df.loc[:, 'Interest Paid'].values


# In[6]:


month


# In[7]:


type(month)


# In[8]:


interestpaid


# In[9]:


type(interestpaid)


# In[10]:


balancedue = df.loc[:, 'New Balance'].values
principalpaid = df.loc[:, 'Principal Paid'].values


# In[11]:


np.sort(balancedue)


# In[28]:


principalpaid[::-1].sort()
principalpaid


# In[13]:


plt.plot(month, interestpaid)


# In[14]:


plt.style.available


# In[15]:


plt.style.use('Solarize_Light2')


# In[16]:


plt.plot(month, interestpaid)


# In[17]:


plt.plot (month, interestpaid, c= 'k', marker = '.', markersize =10)


# In[18]:


plt.plot (month, interestpaid, c= 'b', marker = '.', markersize =10)


# In[19]:


Label_SIZE = 15
title_SIZE = 20
plt.rc('axes', titlesize=title_SIZE)    
plt.rc('axes', labelsize=Label_SIZE)
plt.xlabel('Month')
plt.ylabel('Dollars')
plt.title ('Interest and Principal Paid')
plt.plot(month, interestpaid)


# In[20]:


Label_SIZE = 15
title_SIZE = 20
plt.rc('axes', titlesize=title_SIZE)    
plt.rc('axes', labelsize=Label_SIZE)
plt.xlabel('Month')
plt.ylabel('Dollars')
plt.title ('Interest and Principal Paid')
plt.grid()
plt.grid(c='g')
plt.plot(month, interestpaid)


# In[23]:


Label_SIZE = 15
title_SIZE = 20
plt.rc('axes', titlesize=title_SIZE)    
plt.rc('axes', labelsize=Label_SIZE)
fig, axes = plt.subplots(nrows = 1, ncols = 1);
axes.plot(month, interestpaid, c='b',label='interest')
axes.plot(month, interestpaid, c='k',label='month')
plt.legend(bbox_to_anchor=(1.3,0), loc="lower right")
plt.xlabel('Month')
plt.ylabel('Dollars')
plt.title ('Interest and Principal Paid')
plt.grid()
plt.grid(c='g')


plt.plot(month, interestpaid)
plt.tight_layout()
plt.savefig('Desktop/AmalSuthanBigDataStrategies.png', dpi = 300)
plt.show()


# In[ ]:





# In[ ]:




