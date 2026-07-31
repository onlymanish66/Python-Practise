def height(root):
    if root is None:
        return -1
    l = height(root.left)+1
    r = height(root.right)+1
    return max(l,r)
