def Diameter(root):
    maxx = 0
    height(root)      #calling function height
    def height(root):
        nonlocal maxx      # it will keep modifying maxx value and contain prevoius 
        if root == None:                # value until it modified.
            return -1
        left = height(root.left)+1
        right = height(root.right)+1

        maxx = max(maxx,left+right)
        return max(left,right)

    return maxx
