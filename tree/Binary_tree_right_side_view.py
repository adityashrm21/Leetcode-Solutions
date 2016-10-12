# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        maxlev=0
        ans=[]
        self.right(root, 1, ans)
        return ans
        
    def right(self, root, level, ans):
        if not root:
            return []
        if level>len(ans):
            ans.append(root.val)

        self.right(root.right, level+1, ans)
        self.right(root.left, level+1, ans)
        
        return ans
        