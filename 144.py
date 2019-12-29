# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        #first approach recursive solution 上左右
        """
        if root==None:
            return result
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
        """
        #second approach iterative solution
        result=[]
        stack=[]
        if root==None:
            return result
        stack.append(root)
        while stack:
            root=stack.pop()
            result.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return result