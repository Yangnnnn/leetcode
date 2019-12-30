# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #bfs with depth so we can track which list we should put the node in.
        q=queue.Queue()
        q.put((root,1))
        result=[]
        if root==None:
            return []
        while q.qsize()>0:
            temp,depth=q.get()
            while len(result)<depth:
                result.append([])
            
            result[depth-1].append(temp.val)
            if temp.left:
                q.put((temp.left,depth+1))
            if temp.right:
                q.put((temp.right,depth+1))
        return result
            
        
        
        
        
