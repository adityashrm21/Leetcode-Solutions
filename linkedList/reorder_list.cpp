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

ListNode* reverse(ListNode *A)
{
    if(A==NULL || A->next==NULL)
    return A;
    
    ListNode *temp=A, *prev=NULL,*nex;
    while(temp)
    {
        nex=temp->next;
        temp->next=prev;
        prev=temp;
        temp=nex;
    }
    
    return prev;
}

/*void swap(ListNode **A, ListNode **B)
{
    ListNode **temp=*A;
    *A=*B;
    *B=temp;
}*/

ListNode* reorderList(ListNode* A) {
    
    if(!A || !A->next)
    return A;
    
    if(A->next->next==NULL)
    {
        return A;
    }
    
    ListNode *temp,*fast=A, *slow=A, *prev=NULL, *rev, *mid=NULL, *nex;
    
    while(fast && fast->next && fast->next->next)
    {
        prev=slow;
        slow=slow->next;
        fast=fast->next->next;
    }
    
    if(fast->next!=NULL)
    {
        prev=slow;
        slow=slow->next;
        
    }
    else
    {
        mid=slow;
        slow=slow->next;
        mid->next=NULL;
    }
    
    prev->next=NULL;
    rev=reverse(slow);
    temp=A;
    while(rev)
    {
        nex=A->next;
        A->next=rev;
        A=A->next;
        rev=nex;

    }
    
    if(mid)
    {
        A->next=mid;
    }
    
    return temp;
    
}

};