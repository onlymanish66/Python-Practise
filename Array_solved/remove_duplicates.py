def remove_duplicates(num:list[int])->list[int]:
    "if we want withoout using extra space"
    num.sort()
    i = 0
    for j in range (1,len(num)):
        if num[j] != num[i]:
            i+=1
            num[i] = num[j]
    return num[:i+1]

num = [1,1,2,2,3,4,4,5]
print(remove_duplicates(num))

"if we want to use extra space we can use hashing"