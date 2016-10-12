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
    vector<int> preorderTraversal(TreeNode* root) {
        
        stack<TreeNode *> q;
        
        q.push(root);
        vector<int> ans;
        if(!root)
        return ans;
        while(!q.empty())
        {
            TreeNode *temp=q.top();
            q.pop();
            ans.push_back(temp->val);
            
            if(temp->right)
            q.push(temp->right);
            if(temp->left)
            q.push(temp->left);
        }
        
        return ans;
    }
};