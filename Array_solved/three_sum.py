def three_sum(num:list[int])->list[list[int]]:
    num.sort()
    res = []
    for i in range(len(num)-2):
        if num[i]>0:
            break         # when our target to find 0, bcoz sum 0 will not encounter when num[i] element greater than 0.
        if i>0 and num[i] == num[i-1]:
            continue      #skip duplicates

        l,r = i+1,len(num)-1
        while l<r:
            total = num[i]+num[l]+num[r]
            if total<0:
                l+=1
            elif total>0:
                r-=1
            else:   #when target is 0 or k
                res.append([num[i],num[l],num[r]])

                while l<r and num[l]==num[l+1]:
                    l+=1                            #remove duplicates
                while l<r and num[r]==num[r-1]:
                    r-=1                            #remove duplicates
                l+=1
                r-=1
    return res

num = [-1,-3,0,-2,3,-6]
print(three_sum(num))