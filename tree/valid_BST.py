# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.validate(root, -pow(2,31)-1, pow(2,31)+1)
    
    def validate(self, root, mn, mx):
        
        if root==None:
            return True

        if root.val>=mx or root.val<=mn:
            return False
        
        else:
            #print "dd"
            return self.validate(root.left, mn, root.val) and self.validate(root.right, root.val, mx)
        
        