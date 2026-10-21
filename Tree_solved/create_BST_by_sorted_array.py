class TreeNode:
    def __init__(self,item = 0,left = None,right = None):
        self.item = item
        self.left = left
        self.right = right


def Create_tree_by_sorted_array(nums,left,right):
    if left>right:
        return None
    mid = left+(right-left)//2
    root = TreeNode(nums[mid])
    root.left= Create_tree_by_sorted_array(nums,left,mid-1)
    root.right= Create_tree_by_sorted_array(nums,mid+1,right)

    return root