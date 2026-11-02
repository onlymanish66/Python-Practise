# check tree is mirror image of itself

def Symmetric_tree(root):
    if root is None:
        return True

    def helper(p,q):
        if not p and not q:
            return True
        elif not p or not q or p.item != q.item:
            return False

        left = helper(p.left,q.right)
        right = helper(p.right,q.left)

        return left and right

    return helper(root.left,root.right)
