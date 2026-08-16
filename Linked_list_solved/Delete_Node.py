def deleteNode(start, position):
    # Write your code here
    temp = start
    count = 0
    if count == position:
        start = start.next
    else:
        count = 1
        while count != position:
            temp = temp.next
            count += 1
        temp.next = temp.next.next
    return start