def move_zeroes(arr):
    i = -1
    for j in range(len(arr)):
        if arr[j] != 0:
            i+=1
            arr[j],arr[i] = arr[i],arr[j]
    return arr

arr =[0,5,0,8,3,0,9]
print(move_zeroes(arr))