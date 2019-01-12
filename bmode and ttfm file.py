
# coding: utf-8

# In[34]:


import os
os.chdir("C:\\Users\\Mohit\\Desktop\\folder")


# In[71]:


import matplotlib.pyplot as plt
import pydicom
from pydicom.data import get_testdata_files
bmode = get_testdata_files("bmode.dcm")
bmode=pydicom.read_file('bmode.dcm',force=True)


# In[90]:


bmode


# In[95]:


a = open('bmode.txt', 'w')
a.write('bmode')
a.close()


# In[66]:


ttfm = get_testdata_files("ttfm.dcm")
ttfm=pydicom.read_file('ttfm.dcm',force=True)


# In[67]:


ttfm

