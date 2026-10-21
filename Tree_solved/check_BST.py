def check_BST(root):
    res = []
    inorder(root)            #calling function inorder traversal to check tree is
    def inorder(root):                             #Binary Search  Tree
        if root == None:
            return
        inorder(root.left)
        res.append(root.item)
        inorder(root.right)

    for i in range(1,len(res)):     #checking res is in ascending order
        if res[i] <= res[i-1]:
            return False

    return True