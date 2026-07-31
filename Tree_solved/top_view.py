
def topView(root):
    q=[]
    ele = dict()
    root.level = 0   #create self.level = 0 in node
    q.append(root)
    while len(q)!=0:
        root = q.pop(0)
        if root.level not in ele:
            ele[root.level] = root.info
        if root.left is not None:
            q.append(root.left)
            root.left.level = root.level-1
        if root.right is not None:
            q.append(root.right)
            root.right.level = root.level+1
    for i in sorted(ele):
        print(ele[i],end=" ")