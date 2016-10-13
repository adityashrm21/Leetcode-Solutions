# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if head:
            count=0
        else: return None
        l=head
        while l:
            l=l.next
            count+=1
        print count
        
        k=k%count
        if k==0:
            return head
            
        temp=head
        while k and temp:
            temp=temp.next
            k-=1
        
        prev=None
        temp1=head
        while temp:
            prev=temp1
            temp=temp.next
            temp1=temp1.next
        
        prev.next=None
        temp2=temp1
        
        while temp1 and temp1.next:
            temp1=temp1.next
        
        if temp1:
            temp1.next=head
    
        return temp2
            
        