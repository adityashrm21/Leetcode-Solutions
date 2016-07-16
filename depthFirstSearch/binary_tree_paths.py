# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root==None:
            return []
        #s=str(root.val)
        s=""
        return self.paths(root, s,[])
        
    def paths(self, root, s, ans):
        if root==None:
            return []
        if root.left==None and root.right==None:
            s+=str(root.val)
            ans.append(s)
            
        s+=str(root.val)+"->"

        
        
        self.paths(root.left, s,ans)
        self.paths(root.right,s,ans)
        
        return ans