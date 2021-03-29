#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def list_sort(list_strings):
    list_strings.sort(key=len)
    return list_strings


# In[ ]:


list_strings = ['phone', 'cup', 'bottlecap', 'mobile', 'plants', 'mice', 'pen', 'transfer']
print(list_sort(list_strings))

