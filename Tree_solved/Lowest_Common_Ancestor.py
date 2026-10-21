def Lowest_Common_Ancestor(root,p,q):
    if root == None or root.item == p or root.item == q:
        return root

    left = Lowest_Common_Ancestor(root.left,p,q)
    right = Lowest_Common_Ancestor(root.right,p,q)

    if left and right:
        return root     # root == Ancestor ,here we return
    if left == None:   
        return right   
    else:
        return left
    