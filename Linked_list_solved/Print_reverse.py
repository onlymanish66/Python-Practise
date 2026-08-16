def reversePrint(start):
    # Write your code here
    temp = start
    if temp is None:
        return
    reversePrint(temp.next)
    print(temp.data)