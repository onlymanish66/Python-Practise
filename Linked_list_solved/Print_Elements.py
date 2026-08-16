
def printLinkedList(head):
    if head is None:
        return
    print(head.data)
    printLinkedList(head.next)