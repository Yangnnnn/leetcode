# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #if the root is q , then the LCA must be q. Same for p. 
        if root==None or root==q or root==p:
            return root
        # do recursion here
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        #cases
        #if we find something in left and something in right. then this root must be LCA
        if left and right:
            return root
        
        elif left:
            return left
        elif right:
            return right
