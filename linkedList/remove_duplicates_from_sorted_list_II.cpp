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

ListNode* deleteDuplicates(ListNode* A) {

    if(A==NULL || A->next==NULL)
    return A;
    int flag=0, flag2=0;
    ListNode *dum= new ListNode(A->val-1);
    ListNode *one=dum,*two=A, *three=A->next, *nhead=dum;

    while(two)
    {
        if(one->val!=two->val && (!three || two->val!=three->val))
        {
            dum->next=two;
            dum=two;
            dum->next=NULL;
            
        }
        one=two;
        two=three;
        if(three)
        three=three->next;
        
    }
    return nhead->next;
}
};