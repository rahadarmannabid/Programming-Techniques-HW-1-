#!/usr/bin/env python
# coding: utf-8

# In[22]:


def merge_sort(A, left, right):
    if left < right:  
        mid  = left + (right - left) //2 
        print(A[left: right + 1], left, mid, right)
        merge_sort(A, left, mid )
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)


# In[23]:


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        

    i = 0     
    j = 0     
    k = l     
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
   
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    print(arr)


# In[24]:


arr = [ 3, 1, 4 , 1, 2, 9, 0, 10]
length = len(arr)
n = length - 1
b = [None] * length
merge_sort(arr, 0 , n)


# In[ ]:




