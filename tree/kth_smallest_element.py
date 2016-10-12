# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countnodes(self, root):
        
        if not root:
            return 0
        
        l=self.countnodes(root.left)
        r=self.countnodes(root.right)
        return 1+l+r
        
    def kthSmallest(self, root, k):
        
        return self.getkth(root,k)
        
    def getkth(self, root, k):
        
        #if not root
        cc=self.countnodes(root.left)
        
        if 1+cc==k:
            return root.val
        elif 1+cc>k:
            return self.getkth(root.left, k)
        else:
            return self.getkth(root.right, k-1-cc)
        
    
        