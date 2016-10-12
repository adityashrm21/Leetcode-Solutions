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
    vector<int> inorderTraversal(TreeNode* root) {
        
        stack<TreeNode *> s;

        int done=0;
        vector<int> ans;
        TreeNode *curr=root;
        if(!root) return ans;
        
        while(!done)
        {
            if(curr)
            {    
                s.push(curr);
                curr=curr->left;
            }
            else
            {
                if(!s.empty())
                {curr=s.top();
                s.pop();
                ans.push_back(curr->val);
                curr=curr->right;
                }
                else done=1;
            }
                
        }
        return ans;
    }
};