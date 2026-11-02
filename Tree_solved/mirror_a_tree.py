# Invert or Mirror a binary tree by swapping its nodes

def Mirror(root):
    if not root:
        return

    Mirror(root.left)
    Mirror(root.right)

    root.left,root.right = root.right,root.left   # Swapping nodes