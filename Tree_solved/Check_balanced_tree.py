# the height difference between left and right suntree must be 1 for every node

def balanced_tree(root):
    if not root:
        return True

    def height(root):
        if not root:
            return 0

        left_h = height(root.left)
        if left_h == -1:            #it will not go for next node return from here
            return -1
        right_h= height(root.right)
        if right_h == -1:
            return -1               #it will not go for next node return from here

        if abs(left_h - right_h)>1:
            return -1
        return max(left_h,right_h)+1

    res = height(root)
    if res == -1:
        return False
    else:
        return True