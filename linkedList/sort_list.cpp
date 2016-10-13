/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:

    ListNode* merge(ListNode *h1, ListNode *h2)
    {
        ListNode *d=new ListNode(0);
        ListNode *e=d;
        
        while(h1 || h2)
        {
            if(h1 && (!h2 || (h1->val<=h2->val)))
            {
                e->next=h1;
                e=e->next;
                h1=h1->next;
            }
            
            if(h2 && (!h1 || (h2->val<h1->val)))
            {
                e->next=h2;
                e=e->next;
                h2=h2->next;
            }
        }
        
        e->next=NULL;
        return d->next;
        
    }
  
    ListNode* sortList(ListNode* head) {
        
        if(!head || !(head->next))
        return head;
        
        ListNode *fast=head->next, *slow=head;
        
        while(fast && fast->next)
        {
            fast=fast->next->next;
            slow=slow->next;
        }
        
        ListNode *headb=slow->next;
        slow->next=NULL;
        
        return merge(sortList(head), sortList(headb));
    }
    
};