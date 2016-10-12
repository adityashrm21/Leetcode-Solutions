/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    
    TreeNode * lcautil(TreeNode *root, TreeNode *p, TreeNode *q, bool &v1, bool &v2)
    {
        
        if(!root) return NULL;
        
        if(root==p)
        {
            v1=true;
            return root;
        }
        if(root==q)
        {
            v2=true;
            return root;
        }
        
        TreeNode * l=lcautil(root->left, p,q, v1, v2);
        TreeNode * r=lcautil(root->right, p,q, v1, v2);
        
        if(l && r) return root;
        
        return l!=NULL? l: r;
    }
    
    bool find(TreeNode *root, TreeNode *p)
    {
        if(!root) return NULL;
        
        if(root==p || find(root->left, p) || find(root->right, p))
            return true;
            
        return false;
    }
    
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        
        if(p==q)
        return p;
        
        if(root==NULL) return NULL;
        
        bool v1=false, v2=false;
        
        TreeNode *lca=lcautil(root, p,q, v1, v2);
        
        if(v1&&v2 || v1 &&find(lca, q) || v2 &&find(lca, p))
        return lca;
        
        return NULL;
    }
};