
def reverse(head):
    # Write your code here
    prev = None
    cur = head
    nxt = head.next
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    head = prev
    return head