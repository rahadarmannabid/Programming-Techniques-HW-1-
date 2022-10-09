#!/usr/bin/env python
# coding: utf-8

# In[48]:


import sys
sys.setrecursionlimit(10000)
sys.getrecursionlimit() 



# In[49]:


def Hoare_partition(arr, low, high):
 
    pivot = arr[int((low + high)/2)]
    print("pivot" , pivot)
    i = low - 1
    j = high + 1
    print(i,j)
 
    while (True):
 
        # Find leftmost element greater than
        # or equal to pivot
        i += 1
        while (arr[i] < pivot):
            i += 1
            #print(i, arr[i])
 
        # Find rightmost element smaller than
        # or equal to pivot
        j -= 1
        while (arr[j] > pivot):
            j -= 1
            #print(j, arr[j])
 
        # If two pointers met.
        if (i >= j):
            print("new pivot", j , arr[j])
            return j
        
        print("i,j:", i, j)
 
        arr[i], arr[j] = arr[j], arr[i]
        print(arr)
    
 


# In[50]:


def Quick_sort(A , start, end):
    
    if start < end: 
        pivot =  Hoare_partition(A, start, end)
        Quick_sort(A, start, pivot)
        Quick_sort(A, pivot+1 , end)
        
        


# In[51]:


A = [4, 1 , 2, 0 , 1]
n = len(A)
Quick_sort(A, 0 , n-1)
print(A)


# In[ ]:





# In[ ]:




