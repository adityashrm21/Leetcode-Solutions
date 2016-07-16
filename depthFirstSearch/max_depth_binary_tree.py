# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.depth(root, 1)
        
    def depth(self, root, maxlev):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return maxlev

        return max(self.depth(root.left, maxlev+1) , self.depth(root.right, maxlev+1))
        