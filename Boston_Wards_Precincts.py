#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tabula
import pandas
from tabula import read_pdf  


# In[3]:


bos = ("https://www.boston.gov/sites/default/files/file/2021/11/2021-11-02-21-Mayor.pdf")  #data source


# In[4]:


mayor1 = tabula.read_pdf(bos, pages='2') #reading each page


# In[5]:


mayor2 = tabula.read_pdf(bos, pages='3') 


# In[6]:


mayor3 = tabula.read_pdf(bos, pages='4') 


# In[7]:


mayor4 = tabula.read_pdf(bos, pages='5') 


# In[8]:


mayor5 = tabula.read_pdf(bos, pages='6') 


# In[9]:


mayor6 = tabula.read_pdf(bos, pages='7') 


# In[10]:


mayor7 = tabula.read_pdf(bos, pages='8') 


# In[11]:


mayor8 = tabula.read_pdf(bos, pages='9') 


# In[12]:


mayor9 = tabula.read_pdf(bos, pages='10') 


# In[13]:


mayor10 = tabula.read_pdf(bos, pages='11') 


# In[14]:


mayor11 = tabula.read_pdf(bos, pages='12') 


# In[15]:


mayor12 = tabula.read_pdf(bos, pages='13') 


# In[16]:


mayor13 = tabula.read_pdf(bos, pages='14') 


# In[17]:


mayor14 = tabula.read_pdf(bos, pages='15') 


# In[18]:


mayor15 = tabula.read_pdf(bos, pages='16') 


# In[19]:


mayor16 = tabula.read_pdf(bos, pages='17') 


# In[20]:


mayor17 = tabula.read_pdf(bos, pages='18') 


# In[21]:


mayor18 = tabula.read_pdf(bos, pages='19') 


# In[22]:


mayor19 = tabula.read_pdf(bos, pages='20') 


# In[23]:


mayor20 = tabula.read_pdf(bos, pages='21') 


# In[24]:


mayor21 = tabula.read_pdf(bos, pages='22') 


# In[25]:


mayor22 = tabula.read_pdf(bos, pages='23') 


# In[26]:


m1=mayor1[0] 
m1.rename(columns={'CANDIDATES':'Wards'},inplace=True)


# In[27]:


m_1=m1.set_index(["Wards",m1.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward1


# In[28]:


m_1=m_1.drop('TOTAL', axis=0) #dropping total from the rows 


# In[29]:


m2=mayor2[0] 
m2.rename(columns={'CANDIDATES':'Wards'},inplace=True)


# In[30]:


m_2=m2.set_index(["Wards",m2.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward2


# In[31]:


m_2=m_2.drop('TOTAL', axis=0)


# In[32]:


m3=mayor3[0] 
m3.rename(columns={'CANDIDATES':'Wards'},inplace=True)


# In[33]:


m_3=m3.set_index(["Wards",m3.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward3


# In[34]:


m_3=m_3.drop('TOTAL', axis=0)


# In[35]:


m4=mayor4[0] 
m4.rename(columns={'CANDIDATES':'Wards'},inplace=True)


# In[36]:


m_4=m4.set_index(["Wards",m4.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward4


# In[37]:


m_4=m_4.drop('TOTAL', axis=0)


# In[38]:


m5=mayor5[0] 
m5.rename(columns={'CANDIDATES':'Wards'},inplace=True)


# In[39]:


m_5=m5.set_index(["Wards",m5.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward5


# In[40]:


m_5=m_5.drop('TOTAL', axis=0)


# In[41]:


m6=mayor6[0] 
m6.rename(columns={'CANDIDATES':'Wards'},inplace=True)


# In[42]:


m_6=m6.set_index(["Wards",m6.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward6


# In[43]:


m_6=m_6.drop('TOTAL', axis=0)


# In[44]:


m7=mayor7[0] 
m7.rename(columns={'CANDIDATES':'Wards'},inplace=True)


# In[45]:


m_7=m7.set_index(["Wards",m7.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward7


# In[46]:


m_7=m_7.drop('TOTAL', axis=0)


# In[47]:


m8=mayor8[0] 
m8.rename(columns={'CANDIDATES':'Wards'},inplace=True)


# In[48]:


m_8=m8.set_index(["Wards",m8.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward8


# In[49]:


m_8=m_8.drop('TOTAL', axis=0)


# In[50]:


m9=mayor9[0] 
m9.rename(columns={'CANDIDATES':'Wards'},inplace=True)


# In[51]:


m_9=m9.set_index(["Wards",m9.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward9


# In[52]:


m_9=m_9.drop('TOTAL', axis=0)


# In[53]:


m10=mayor10[0] 
m10.rename(columns={'CANDIDATES':'Wards'},inplace=True)


# In[54]:


m_10=m10.set_index(["Wards",m10.groupby("Wards").cumcount()]).unstack().T.droplevel(1)  #ward10


# In[55]:


m_10=m_10.drop('TOTAL', axis=0)


# In[56]:


m11=mayor11[0] 
m11.rename(columns={'CANDIDATES':'Wards'},inplace=True)


# In[57]:


m_11=m11.set_index(["Wards",m11.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward11


# In[58]:


m_11=m_11.drop('TOTAL', axis=0)


# In[59]:


m12=mayor12[0] 
m12.rename(columns={'CANDIDATES':'Wards'},inplace=True)


# In[60]:


m_12=m12.set_index(["Wards",m12.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward12


# In[61]:


m_12=m_12.drop('TOTAL', axis=0)


# In[62]:


m13=mayor13[0] #ward14
m13.rename(columns={'CANDIDATES':'Wards'},inplace=True)


# In[63]:


m_13=m13.set_index(["Wards",m13.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward13


# In[64]:


m_13=m_13.drop('TOTAL', axis=0)


# In[65]:


m14=mayor14[0] #ward14
m14.rename(columns={'CANDIDATES':'Wards'},inplace=True)
 


# In[66]:


m_14=m14.set_index(["Wards",m14.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward14


# In[67]:


m_14=m_14.drop('TOTAL', axis=0)


# In[68]:


m15=mayor15[0]  
m15.rename(columns={'CANDIDATES':'Wards'},inplace=True) 


# In[69]:


m_15=m15.set_index(["Wards",m15.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward15


# In[70]:


m_15=m_15.drop('TOTAL', axis=0)


# In[71]:


m16=mayor16[0]   
m16.rename(columns={'CANDIDATES':'Wards'},inplace=True)
 


# In[72]:


m_16=m16.set_index(["Wards",m16.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward16


# In[73]:


m_16=m_16.drop('TOTAL', axis=0)


# In[74]:


m21=mayor21[0]  
m21.rename(columns={'CANDIDATES':'Wards'},inplace=True)
   


# In[75]:


m_21=m21.set_index(["Wards",m21.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward21


# In[76]:


m_21=m_21.drop('TOTAL', axis=0)


# In[77]:


m22=mayor22[0]  
m22.rename(columns={'CANDIDATES':'Wards'},inplace=True)
  


# In[78]:


m_22=m22.set_index(["Wards",m22.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward22


# In[79]:


m_22=m_22.drop('TOTAL', axis=0)


# In[80]:


m20=mayor20[0]  
m20.rename(columns={'CANDIDATES':'Wards'},inplace=True)


# In[81]:


m_20=m20.set_index(["Wards",m20.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward20


# In[82]:


m_20=m_20.drop('TOTAL', axis=0)


# In[83]:


m19=mayor19[0]  
m19.rename(columns={'CANDIDATES':'Wards'},inplace=True)
 


# In[84]:


m_19=m19.set_index(["Wards",m19.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward19


# In[85]:


m_19=m_19.drop('TOTAL', axis=0)


# In[86]:


m18=mayor18[0]  
m18.rename(columns={'CANDIDATES':'Wards'},inplace=True)
 


# In[87]:


m_18=m18.set_index(["Wards",m18.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward18


# In[88]:


m_18=m_18.drop('TOTAL', axis=0)


# In[89]:


m17=mayor17[0]  
m17.rename(columns={'CANDIDATES':'Wards'},inplace=True)
 


# In[90]:


m_17=m17.set_index(["Wards",m17.groupby("Wards").cumcount()]).unstack().T.droplevel(1) #ward17


# In[91]:


m_17 = m_17.drop('TOTAL', axis=0)


# In[92]:


wards_precincts = pandas.concat([m_1,m_2,m_3,m_4,m_5,m_6,m_7,m_8,m_9,m_10,m_11,m_12,m_13,
                                m_14,m_15,m_16,m_17,m_18,m_19,m_20,m_21,m_22]) #joining all the dataframes


# In[93]:


wards_precincts=wards_precincts.drop('Unnamed: 0', axis=0) #removing NaN


# In[99]:


first_col=['ANNISSA ESSAIBI GEORGE','MICHELLE WU','ALL OTHERS','BLANKS','BALLOTS CAST','VOTES CAST'] 
wards_precincts=wards_precincts[first_col]


# In[101]:


wards_precincts.to_csv('2021_Bos_wards_precincts.csv')  #saving to csv

