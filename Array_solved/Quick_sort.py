
# Quick Sort

def quick_sort(arr,left,right):
    if left<right:
        index = partition(arr,left,right)
        quick_sort(arr,left,index-1)
        quick_sort(arr,index+1,right)

def partition(arr,left,right):
    pivot = arr[right]
    temp_index = left -1
    while left<right:
        if arr[left] < pivot:
            temp_index+=1
            arr[temp_index],arr[left] = arr[left],arr[temp_index]
        left+=1
    arr[temp_index+1],arr[right] = arr[right],arr[temp_index+1]
    return temp_index+1

arr = [5,8,3,2,7,9,4]
quick_sort(arr,0,len(arr)-1)
print(arr)