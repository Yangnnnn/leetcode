# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ##recursive solution
        #if root ==None:
            #return 0
        #return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
        
        #iterative solution when append the root to stack,we update depth+1
        if root==None:
            return 0
        max_depth=0
        stack=[]
        stack.append((root,1))
        while stack: 
            root,depth = stack.pop()
            if depth>max_depth:
                max_depth=depth
            if root.left:
                stack.append((root.left,depth+1))
            if root.right:
                stack.append((root.right,depth+1))
        return max_depth
