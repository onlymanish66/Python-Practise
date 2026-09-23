def rotateLeft(rotate, arr):
    rotate%=len(arr)
    return arr[rotate:] + arr[:rotate]

arr=[1,2,3,4,5]
res= rotateLeft(13,arr)
print(res)