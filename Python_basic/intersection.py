def intersection_Array(arr1,arr2):
    res = [x for x in arr1 if x in arr2]
    return res


arr1 = [2,4,7,5,9]
arr2 = [3,7,6,2,1]
print(intersection_Array(arr1,arr2))

"print(set(arr1)&set(arr2))"