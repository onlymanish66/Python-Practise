def find_pairs(target,arr):
    seen = {}
    for index in range(len(arr)):
        complement = target-arr[index]
        if complement in seen:
            return (seen[complement],index)
        seen[arr[index]] = index
    return "No Pairs"
    

arr = [1,4,3,2,6,4,7]
target = 6
res = find_pairs(target,arr)
print(res)