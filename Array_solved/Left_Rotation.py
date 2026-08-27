def rotateLeft(rotate, arr):
    newarray = []
    newarray = arr[rotate:] + arr[:rotate]
    return newarray

arr=[1,2,3,4,5]
res= rotateLeft(2,arr)
print(res)