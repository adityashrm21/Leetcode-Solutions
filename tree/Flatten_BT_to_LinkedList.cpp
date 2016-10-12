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
    void flatten(TreeNode* root) {
        TreeNode *temp=root;
        
        while(temp)
        {
            if(temp->left)
            {
                TreeNode *pre=temp->left;
                while(pre->right)
                pre=pre->right;
                pre->right=temp->right;
                temp->right=temp->left;
                temp->left=NULL;
            }
            temp=temp->right;
        }
    }
};