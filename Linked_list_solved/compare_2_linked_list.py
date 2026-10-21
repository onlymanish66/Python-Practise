def compare_lists(head1, head2):
    temp1 = head1
    temp2 = head2
    while temp1 and temp2:
        if temp1.data != temp2.data:
            return 0
        temp1 = temp1.next
        temp2 = temp2.next
    if temp1==temp2:
        return 1
    else:
        return 0