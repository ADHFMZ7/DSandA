#python implementation of merge sort

import random

nums = [random.randint(0, 100) for i in range(100)]
nums2 = [random.randint(0, 100) for i in range(10)]



def merge(arr1, arr2):
  result = []
  while len(arr1) or len(arr2):
    if len(arr1) and len(arr2):
      result.append(arr1.pop(0)) if arr1[0] <= arr2[0] else result.append(arr2.pop(0))
    elif len(arr1):
      result.append(arr1.pop(0))
    elif len(arr2):
      result.append(arr2.pop(0))
  return result 

def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  return merge(mergeSort(arr[:len(arr)//2]), mergeSort(arr[len(arr)//2:]))

print(sorted(nums) == mergeSort(nums))