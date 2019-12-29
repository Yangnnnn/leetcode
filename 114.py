# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #上左右  preorder
        temp=self.helper(root)
        for i in range(len(temp)):
            
            root.val=temp[i]
            if i==len(temp)-1:
                break
            root.left=None
            if root.right:
                root=root.right
            else:
                root.right=TreeNode(0)
                root=root.right
            
            
    
    def helper(self,root):
        if root==None:
            return []
        return [root.val]+self.helper(root.left)+self.helper(root.right)
