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


ListNode* addTwoNumbers(ListNode* A, ListNode* B) {

    ListNode *t1=A, *t2=B, *prev=NULL, *head=NULL;
    
    int carry=0, sum=0;
    
    if(!A)
    return B;
    if(!B) return A;
    
    while(t1 || t2)
    {
        
        sum=(t1?t1->val:0)+(t2?t2->val:0)+carry;
        //cout<<"sum: "<<sum<<endl;
        carry=(sum>9)?1:0;
        //cout<<"carry: "<<carry<<endl;
        sum=sum%10;
        ListNode *temp= new ListNode(sum);
        
        if(!head)
        {
            head=temp;
        }
        else
        {
            prev->next=temp;
            
        }
        prev=temp;
        
        if(t1) t1=t1->next;
        if(t2) t2=t2->next;
        
        //cout<<"fff"<<endl;
        
    }
    if(carry)
    {
        ListNode *temp=new ListNode(carry);
        prev->next=temp;
    }
    
    return head;
}

};