# check both trees are same

def Identical_trees(root1,root2):
    if not root1 and not root2:        # if both nodes are None
        return True
    elif not root1 or not root2 or root1.item != root2.item:  #if any of node is None
        return False

    left = Identical_trees(root1.left,root2.left)
    right = Identical_trees(root1.right,root2,right)

    return left and right  # if both True return True else return False