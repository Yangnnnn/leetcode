# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.summ=0
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.helper(root)
        return root
    
    def helper(self,root):
        #设置一个当前的sum 从右边->上->左
        if root==None:
            return
        if root.right:
            self.convertBST(root.right)
        root.val=root.val+self.summ
        self.summ=root.val
        if root.left:
            self.convertBST(root.left)
        
        
        
        
