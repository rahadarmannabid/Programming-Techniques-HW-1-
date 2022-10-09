import random
import time

def insert_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i>= 0 and A[i]> key:
            A[i+1] = A[i]
            i = i - 1
        A[i + 1] = key
    print(A)


Best_case = [1, 2, 6 , 7 , 8 , 9]
worst_case = [9, 8 , 7, 6, 2, 1]
avg_case = [1, 2 , 6, 9 , 8 , 7]


st = time.time()
insert_sort(Best_case) 
et = time.time()
elapsed_time = et - st
print('Best Execution time:', elapsed_time, 'seconds')

st = time.time()
insert_sort(worst_case) 
et = time.time()
elapsed_time = et - st
print('Worst Execution time:', elapsed_time, 'seconds')

st = time.time()
insert_sort(avg_case) 
et = time.time()
elapsed_time = et - st
print('Avg Execution time:', elapsed_time, 'seconds')