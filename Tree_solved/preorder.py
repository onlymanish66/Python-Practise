"Preorder Traversal"

class node:
    def __init__(self,item = None,left = None,right = None):
        self.item = item
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def InsertData(self,data):
        self.root = self.rinsert(self.root,data)


    def rinsert(self,root,data):
        if root == None:
            return node(data)
        if data < root.item:
            root.left = self.rinsert(root.left,data)
        elif data> root.item:
            root.right = self.rinsert(root.right,data)
        return root

    def preorder(self,root):
        if root == None:
            return
        print(root.item)
        self.preorder(root.left)
        self.preorder(root.right)



bin = BST()
bin.InsertData(70)
bin.InsertData(20)
bin.InsertData(145)
bin.InsertData(139)
bin.InsertData(60)
bin.InsertData(73)
bin.InsertData(24)
bin.preorder(bin.root)