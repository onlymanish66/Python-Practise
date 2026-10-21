def Reverse_DLL(head):
    curr = head
    p = None
    while curr:
        temp = curr.next
        curr.next = p
        p = curr
        curr.prev = temp
        curr = temp
    return p

