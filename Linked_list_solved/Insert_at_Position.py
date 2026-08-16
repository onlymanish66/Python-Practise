def insertNodeAtPosition(start, data, position):
    # Write your code here
    n = SinglyLinkedListNode(data)
    temp = start
    if start == None:
        start = n

    else:
        count = 1
        while temp != None and count<position:
            temp = temp.next
            count += 1
        n.next = temp.next
        temp.next = n
    return start