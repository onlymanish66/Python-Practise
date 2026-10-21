def levelOrder(root):
    #Write your code here
    q = []
    ele = []
    if root == None:
        return
    q.append(root)
    ele.append(root.info)
    while len(q)!=0:
        root = q.pop(0)
        if root.left is not None:
            q.append(root.left)
            ele.append(root.left.info)
        if root.right is not None:
            q.append(root.right)
            ele.append(root.right.info)
    print(*ele)