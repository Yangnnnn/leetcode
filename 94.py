# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #first approach iterative solution 左上右
        """
        if root==None:
            return[]
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
        """
        #second approach iterative solution 把左边全部先放进去 然后每次pop看右边
        result=[]
        stack=[]
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            temp=stack.pop()
            if temp:
                result.append(temp.val)
                if temp.right:
                    root=temp.right
        return result