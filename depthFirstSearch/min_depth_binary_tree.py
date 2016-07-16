# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.depth(root, 1)
        
    def depth(self, root, minlev):
        if root==None:
            return 0
        l=99999
        r=99999
        if root.left==None and root.right==None:
            return minlev
        if root.left:
            l=self.depth(root.left, minlev+1)
        if root.right:
            r=self.depth(root.right, minlev+1)
        return min(l,r)
        