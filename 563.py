# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def findTilt(self, root: TreeNode) -> int:
        self.tilt=0
        self.helper(root)
        return self.tilt
        
    def helper(self,root):
        #实际上这个function算的是这个点的sum 只是在过程中我们在update tilt
        if root==None:
            return 0
        left=self.helper(root.left)
        right=self.helper(root.right)
        self.tilt=self.tilt+abs(left-right)
        return left+right+root.val
        
