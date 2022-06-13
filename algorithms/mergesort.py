#python implementation of merge sort

import random

nums = [random.randint(0, 100) for i in range(100)]
nums2 = [random.randint(0, 100) for i in range(100)]
print(nums)
print(nums2)
def merge(arr1, arr2):
  result = [0]*(len(arr1) + len(arr2))
  m,n = 0,0
  for i in range(len(arr1) + len(arr2)):
    if n+1 == len(arr2) or arr1[m] < arr2[n]:
      result[i] = arr1[m]
      m+=1
    elif m+1 == len(arr1) or arr2[n] < arr1[m]:
      result[i] = arr2[n]
      n+=1
    elif arr2[n] == arr2[m]:
      result[i] = arr1[m]
      m+=1
  return result
    
print(merge(sorted(nums), sorted(nums2)))    

#def mergesort(nums):
  
