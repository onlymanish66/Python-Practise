def sortedInsert(head, data):
    # Write your code here
    n = DoublyLinkedListNode(data)
    temp = head
    if head is None:
        return n 
    if data <= head.data:
        
        n.next = head
        head.prev = n
        head = n
        return head
    while temp:
        if data <= temp.data:
            n.prev = temp.prev
            n.next = temp
            temp.prev.next = n
            temp.prev = n
            return head
        if temp.next is None:
            n.prev = temp
            n.next = None
            temp.next = n
            return head
        temp = temp.next
