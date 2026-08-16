"Search Data in Binary Search  Tree"
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

    def search(self,data):
        return self.rsearch(self.root,data)

    def rsearch(self,root,data):
        if root is None or root.item == data:
            return root
        if data<root.item:
            return self.rsearch(root.left,data)
        else:
            return self.rsearch(root.right,data)
        
        

bin = BST()
bin.InsertData(10)
bin.InsertData(20)
bin.InsertData(30)
bin.search(20)

