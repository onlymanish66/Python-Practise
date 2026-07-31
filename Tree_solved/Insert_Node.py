"Binary Search Tree creation"

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
        print(self.root.item)

    def rinsert(self,root,data):
        if root == None:
            return node(data)
        if data < root.item:
            root.left = self.rinsert(self,root.left,data)
        elif data> root.item:
            root.right = self.rinsert(self,data,root.right)
        return root

bin = BST()
bin.InsertData(10)
bin.InsertData(20)
bin.InsertData(145)
bin.InsertData(139)
bin.InsertData(60)
bin.InsertData(73)
bin.InsertData(24)
