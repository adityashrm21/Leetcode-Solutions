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

    void sumtree(TreeNode *root, int val)
    {
        val=val*10+root->val;
        
        if(root->left==NULL && root->right==NULL)
        {
            sum+=val;    
        }

        if(root->left)
        {
            sumtree(root->left, val);
        }
        if(root->right)
        {
            sumtree(root->right, val);
        }
    }
    int sumNumbers(TreeNode* root) {
        
        if(!root) return 0;
        sum=0;
        sumtree(root, 0);
        return sum;
    }
private:
    int sum;
};

