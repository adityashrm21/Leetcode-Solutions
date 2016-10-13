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

ListNode* reverseBetween(ListNode* A, int m, int n) {
    if(A==NULL || A->next==NULL)
    return A;
    
    int c1=1, c2=1;
    if(m>=n)
    return A;   
    ListNode *temp=A, *cur, *nex, *prev,*first;
    while(c1<m-1 && temp)
    {
        temp=temp->next;
        c1++;
        c2++;
    }
    //cout<<"temp :" << temp->val<<endl;
    if(temp->next && m>1)
    {
        prev=temp->next;
        first=prev;
        c2++;
    }
    else
    {
        //cout<<"yes"<<" ";
        prev=temp;
        first=prev;
    }
    
    if(prev->next)
    cur=prev->next;
    
    
    while(cur && c2<n)
    {
        //cout<<"fffff"<<" ";
        nex=cur->next;
        cur->next=prev;
        prev=cur;
        cur=nex;
        c2++;
    }
    //cout<<first->val<<endl;
    if(first!=A)
    {
        first->next=cur;
        temp->next=prev;
    }
    else
    {
        A=prev;
        first->next=cur;
    }
    
    return A;
    
}


};