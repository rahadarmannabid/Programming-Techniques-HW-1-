#!/usr/bin/env python
# coding: utf-8

# In[63]:


def Count_sort(A):
    
    maximum = max(A) + 1
    
    C = [0] * maximum 
    
    B = [0] * len(A) 
    
    #print(A, B , C)
    
    index = len(A)-1
 
    
    for i in range( 0 , len(A) ):
        C[A[i]]= C[A[i]] + 1
    #print(C)
        
    for j in range( 1 , len(C)):
        C[j] = C[j] + C[j-1]
    #print(C)
    
    for k in range(index , -1, -1):
        #print(k, A[k],C, C[A[k]], B[C[A[k]]-1] )
        B[C[A[k]]-1] = A[k]
        C[A[k]] = C[A[k]] - 1 
    
    return B




# In[64]:


A = [2, 3 , 0 , 1, 7, 9, 2, 1 , 1, 5]
Count_sort(A)


# In[ ]:





# In[ ]:





# In[ ]:




