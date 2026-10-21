def Postorder(root):
    if root is None:
        return
    Postorder(root.left)
    Postorder(root.right)
    print(root.item)