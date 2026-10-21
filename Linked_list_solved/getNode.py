def getNode(head, positionFromTail):
    # Write your code here
    
    fast = head
    slow = head
    for _ in range(positionFromTail):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    return slow.data
    

    
    
    
    # temp = head
    # count = 1
    # length = llist_count - positionFromTail
    # if count == length:
    #     return temp.data
    # while count != length:
    #     temp =temp.next
    #     count = count + 1
    # return temp.data
    