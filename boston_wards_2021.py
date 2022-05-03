#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tabula


# In[2]:


bos = ("https://www.boston.gov/sites/default/files/file/2021/11/2021-11-02-21-Mayor.pdf")  


# In[3]:


mayor = tabula.read_pdf(bos, pages='1')  #first page


# In[4]:


print(mayor[0]) #first table


# In[5]:


mayorbos=mayor[0] 


# In[6]:


mayorbos.rename(columns={'CANDIDATES':'Wards'},inplace=True) #rename the column to wards


# In[7]:


print(mayorbos) #new table with the new column


# In[8]:


mayor_bos=mayorbos.set_index(["Wards",mayorbos.groupby("Wards").cumcount()]).unstack().T.droplevel(1) 


# In[9]:


print(mayor_bos) #transposed table with candidates as columns


# In[11]:


mayor_bos.to_csv("2021_Boston_Mayoral_Wards.csv", index=False) 


# In[ ]:




