#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv("items.csv")
df.columns


# In[2]:


item_list=df['Name']



# In[3]:


new_name_list=map(lambda a: a.replace(" ","%20"),item_list)
new_name_list=list(new_name_list)
new_name_list


# In[4]:


url_name_list=map(lambda a: "https://www.facebook.com/marketplace/category/search/?sortBy=creation_time_descend&daysSinceListed=1&deliveryMethod=local_pick_up&query={}&exact=false".format(a), new_name_list)
url_name_list=list(url_name_list)
url_name_list


# In[5]:


# df["new"]=url_name_list
df.shape


# In[6]:


import webbrowser
import time
sleep_time=df['sleep_time'][0]
for i,url in enumerate(url_name_list):
    webbrowser.open(url)
    print(item_list[i])
    time.sleep(sleep_time)
# In[ ]:




