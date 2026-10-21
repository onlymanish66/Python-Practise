
def findMergeNode(head1, head2):
    temp1 = head1
    while temp1:
        temp2 = head2
        while temp2:
            if temp2 == temp1:
                return temp1.data
            temp2 = temp2.next
        temp1 = temp1.next
        


    # ptr1 = head1
    # ptr2 = head2
    # while ptr1 != ptr2:
    #     if ptr1:
    #         ptr1 = ptr1.next
    #     else:
    #         ptr1 = head2
    #     if ptr2:
    #         ptr2 = ptr2.next
    #     else:
    #         ptr2 = head1
    # return ptr1.data