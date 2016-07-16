# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans=[]
        h=self.height(root)
        for i in range(0,h):
            ans.append(self.getlevel(root, i, []))
        
        return ans
        
        
    def height(self, root):
        if root==None:
            return 0
        else:
            return 1+max(self.height(root.left), self.height(root.right))
    
    def getlevel(self, root, l, arr):
        if root==None:
            return []
        
        if l==0:
            arr.append(root.val)
            
        self.getlevel(root.left, l-1,arr)
        self.getlevel(root.right,l-1,arr)
    
    
        return arr
        
        
        
        
        
        