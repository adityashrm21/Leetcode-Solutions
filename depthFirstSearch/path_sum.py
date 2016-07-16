# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root==None:
            return False
        return self.pathSum(root, sum)
    
    def pathSum(self, root, sum):
        
        if root==None:
            return (sum==0)
        else:
            ans=False
            subsum=sum-root.val
            if subsum==0 and root.left==None and root.right==None:
                return True
            
            if root.left:
                ans= ans or self.pathSum(root.left, subsum)
            if root.right:
                ans=ans or self.pathSum(root.right, subsum)
        
            return ans
                