
def insertNodeAtHead(llist, data):
    # Write your code here
    n = SinglyLinkedListNode(data)
    temp = llist
    if temp is None:
        temp = n
    else:
        n.next = temp
        temp = n
    return temp