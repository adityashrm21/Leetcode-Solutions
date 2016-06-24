# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp1=head
        temp2=head
        
        
        if temp2.next==None and n==1:
            return None
            
        
        while n:
            temp2=temp2.next
            n-=1
        
        while temp2 and temp2.next:
            temp2=temp2.next
            temp1=temp1.next
            #print "hhh"
        if temp2==None:
            head=head.next
            return head
            
        elif temp1 and temp1.next:
            temp3=temp1.next.next
            rem=temp1.next
            temp1.next=temp3
            del rem

        return head
        
        
        
    