/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
public:
    stack<TreeNode *> s;
    BSTIterator(TreeNode *root) {
        while(!s.empty())
        s.pop();
        
        TreeNode* temp=root;
        while(temp)
        {
            s.push(temp);
            temp=temp->left;
        }
        
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !s.empty();
    }

    /** @return the next smallest number */
    int next() {
        TreeNode *temp=s.top();
        s.pop();
        int result=temp->val;
        
        if(temp->right)
        {
            temp=temp->right;
            while(temp)
            {
                s.push(temp);
                temp=temp->left;
            }
        }
        return result;
    }
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */