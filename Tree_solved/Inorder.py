def Inorder(root):
    if root is None:
        return
    Inorder(root.left)
    print(root.item)
    Inorder(root.right)