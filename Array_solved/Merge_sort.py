def merge_sort(list1):
    if len(list1)>1:
        mid = len(list1)//2
        leftlist = list1[:mid]
        rightlist = list1[mid:]

        merge_sort(leftlist)
        merge_sort(rightlist)

        i=j=k=0
        while i<len(leftlist) and j<len(rightlist): #merging sorted lists
            if leftlist[i] < rightlist[j]:
                list1[k] = leftlist[i]
                i+=1
            else:
                list1[k] = rightlist[j]
                j+=1
            k+=1

        while i<len(leftlist):    #remaining element of leftlist
            list1[k] = leftlist[i]       # we can use list1.extend(leftlist[i:]) and for 
                                         # same rightlist
            i+=1
            k+=1
        while j<len(rightlist):
            list1[k] = rightlist[j]
            j+=1
            k+=1

list1 = [5,8,3,2,6,4,1]
merge_sort(list1)
print(list1)        
