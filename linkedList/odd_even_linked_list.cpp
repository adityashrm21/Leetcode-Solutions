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
    ListNode* oddEvenList(ListNode* head) {
     
     ListNode *temp1=head, *temp2,*prev, *h1=head,*h2;
     
     if(head) 
     {
         temp2=head->next;
         h2=head->next;
     }
     else return temp1;
     
     while(temp1!=NULL && temp2!=NULL)
     {
         if(temp2)
         {
             prev=temp1;
             temp1->next=temp2->next;
             temp1=temp1->next;
         }
         if(temp1)
         {
             temp2->next=temp1->next;
             temp2=temp2->next;
         }
     }
     if(temp1)
     {
         temp1->next=h2;
         return h1;
     }
     else
     {
         prev->next=h2;
         return h1;
     }
     return h1;
     
    }
};