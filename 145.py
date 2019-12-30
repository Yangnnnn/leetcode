# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        if root==None:
            return []
        
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]
        """
        stack=[]
        result=[]
        if root==None:
            return []
        stack.append(root)
        while stack:
            temp=stack.pop()
            result.append(temp.val)
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
        result.reverse()
        return result
                
            
