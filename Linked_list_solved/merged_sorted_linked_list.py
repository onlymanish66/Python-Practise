def mergeLists(headA, headB):
    newnode = SinglyLinkedListNode(0)
    start = newnode
    head3 = start
    while True:
        if not headA:
            head3.next = headB
            break
        if not headB:
            head3.next = headA
            break
        if headA.data<=headB.data:
            head3.next = headA
            headA = headA.next
        else:
            head3.next = headB
            headB = headB.next        
        head3 = head3.next
    return start.next
        
        
      
# def mergeLists(headA, headB):
#     if not headA:
#         return headB
#     if not headB:
#         return headA
        
#     # Ek dummy node jo merged linked list ko point kreha starting se ya head
#     dummy = SinglyLinkedListNode(0)
#     headC = dummy  # headC se hum list ko traverse karenge
    
#     # Jab tak dono lists mein elements hain
#     while headA and headB:
#         if headA.data <= headB.data:
#             headC.next = headA  # Naya node banane ki jagah direct purana node joda
#             headA = headA.next
#         else:
#             headC.next = headB  # Purana node joda
#             headB = headB.next
#         headC = headC.next
        
#     # Loop ke baad jo bhi list bachi hai, use bina loop chalaye direct connect kar do
#     if headA:
#         headC.next = headA
#     else:
#         headC.next = headB

#     return dummy.next
            