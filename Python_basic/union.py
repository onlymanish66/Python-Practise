def union_arr(arr1,arr2):
    res = []
    for i in arr1:
        if i not in res:
            res.append(i)
    for j in arr2:
        if j not in res:
            if j not in res:
                res.append(j)

    return res

arr1 = [2,4,7,9,4]
arr2 = [1,4,6,2,3]
print(union_arr(arr1,arr2))