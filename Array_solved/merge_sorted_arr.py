a = list(map(int,input().split()))
b = list(map(int,input().split()))
def merge(a,b):
    i=0
    j=0
    merge_arr = []
    while i<len(a) and j<len(b):
        if a[i] < b[j]:
            merge_arr.append(a[i])
            i+=1
        else:
            merge_arr.append(b[j])
            j+=1
    merge_arr.extend(a[i:])
    merge_arr.extend(b[j:])
    return merge_arr


result = merge(a,b)
print(result)

