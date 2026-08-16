def insertNodeAtTail(head, data):
    n = SinglyLinkedListNode(data)
    temp = head
    if temp is None:
        head = n
    else:
        while temp.next:
            temp = temp.next
        temp.next = n
        
    return head  