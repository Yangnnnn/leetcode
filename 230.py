# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        #左上右  inorder first apporach recursive solution
        """
        lst=self.helper(root)
        return lst[k-1]
        
        
        
    def helper(self,root):
        if root==None:
            return []
        return self.helper(root.left)+[root.val]+self.helper(root.right)
        """
        #second approach iterative solution
        #
        count=0
        stack=[]
        while stack or root:
            
            while root:
                stack.append(root)
                root=root.left
            temp=stack.pop()
            if temp!=None:
                count+=1
                if count==k:
                    return temp.val
                if temp.right:
                    root=temp.right
            
            
