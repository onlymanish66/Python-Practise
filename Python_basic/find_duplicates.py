def find_duplicates(arr):
    seen =[]
    duplicates =[]
    for num in arr:
        if num in seen:
            duplicates.append(num)
        seen.append(num)
    return duplicates

arr = [2,4,2,6,8,4,3]
print(find_duplicates(arr))
