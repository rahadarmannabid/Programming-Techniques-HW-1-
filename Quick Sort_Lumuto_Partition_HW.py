#!/usr/bin/env python
# coding: utf-8

# In[105]:


def lomuto_part(arr, start, end):
    index = end
    key = arr[index]
    i = -1
    for j in range(0,index):
        if arr[j] <= key:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[index] = arr[index], arr[i + 1]

        
            
    return i+1
    
         


# In[106]:


def Quick_sort(A, start, end):
    if start < end: 
        pivot = lomuto_part(A, start, end)
        Quick_sort(A, start , pivot-1 )
        Quick_sort (A, pivot + 1, end)


# In[108]:


A = [2, 4, 3, 3 , 1, 0, 10]
n = len(A)
Quick_sort(A, 0, n-1)
print(A)


# In[ ]:




