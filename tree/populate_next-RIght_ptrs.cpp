/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
        TreeLinkNode *gnr(TreeLinkNode *root)
    {
        TreeLinkNode *temp=root->next;
        while(temp)
        {
            if(temp->left) return temp->left;
            if(temp->right) return temp->right;
            
            temp=temp->next;
            
        }
        return NULL;
    }
        
    void connect(TreeLinkNode *p) 
    {
        if(!p) return;
        
        p->next=NULL;
        
        while(p)
        {
            TreeLinkNode *q=p;
            
            while(q)
            {
                if(q->left)
                {
                    if(q->right)
                    q->left->next=q->right;
                    else
                    {
                        q->left->next=gnr(q);
                    }
                }
                
                if(q->right)
                q->right->next=gnr(q);
                q=q->next;
            }
            
            if(p->left) p=p->left;
            else if(p->right) p=p->right;
            else p=gnr(p);
        }
        return;
        
    }
};