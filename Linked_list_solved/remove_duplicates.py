
def removeDuplicates(head):
    # # Write your code here
    temp = head
    if head == None and head.next == None:
        return head
    while temp.next != None:
        if temp.data == temp.next.data:
            temp.next = temp.next.next
        else:
            temp = temp.next
    return head
        
        


    # temp1 = head
    # temp2 = head
    # if head == None and head.next == None:
    #     return head
    # while temp2.next:
    #     if temp1.data != temp2.next.data:
    #         temp1.next = temp2.next     #skip duplicates and join distinct node data
    #         temp1 = temp1.next
    #     temp2 = temp2.next
    # temp1.next = None
    # return head