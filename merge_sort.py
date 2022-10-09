import time
import random

def merge_sort(A,left,right):
    if left < right:  
        mid  = left + (right - left) //2 
        print(A[left: right + 1], left, mid, right)
        merge_sort(A, left, mid )
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)



    

def merge(A, left, mid, right):
    i = left - 1
    j = mid + 1
    k = left
    

    while i<= mid and j <= right:
        if A[i] <= A[j]:
            b[k] = A[i]
            i = i + 1
            
            
        else:
            b[k] = A[j]
            j = j + 1
        k = k + 1
        print("b", b)
    

    # print(A, left, mid, right)


A = [1, 4, 6, 2, 3, 2, 4, 5]
n = len(A)
b = [None] * len(A)
merge_sort(A, 0, n-1 )
