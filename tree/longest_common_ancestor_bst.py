# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.lca(root, p,q)
        
    def lca(self, root, p,q):
        if root==None:
            return None
        if root.val<p.val and root.val<q.val:
            return self.lca(root.right, p,q)
        if root.val>p.val and root.val>q.val:
            return self.lca(root.left, p,q)
        
        return root
        