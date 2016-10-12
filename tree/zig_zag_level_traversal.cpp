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

    int height(TreeNode *root)
    {
        if(!root)
        return 0;
        
        return 1+max(height(root->left), height(root->right));
    }
    
    vector<int> util(TreeNode *root, int dir, int level, vector<int> &path)
    {
        
        if(!root) return path;
        if(level==1)
        {
            path.push_back(root->val);
        }
        
        if(dir>0)
        {
            util(root->left, dir, level-1, path);

            util(root->right, dir, level-1, path);
        }
        else
        {
           

            util(root->right, dir, level-1, path);
             util(root->left, dir, level-1, path);
        }
        
        return path;
    }
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
    
        vector<vector<int>> ans;
        if(!root)    
        return ans;
        
        int h=height(root);
        //cout<<"h: "<<h<<endl;
        int dir=1;
        for(int i=1;i<=h;i++)
        {
            vector<int> path;
            ans.push_back(util(root, dir, i,path ));
            dir=-dir;
        }
        
        return ans;
            
        
    }
};