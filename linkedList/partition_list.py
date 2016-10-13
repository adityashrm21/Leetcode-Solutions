# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        t=head
        t1=None
        t2=None
        s=None
        j=None
        
        if t:
            if t.val<x:
                t1=ListNode(t.val)
                s=t1
                t=t.next
                while t and t.val<x:
                    t1.next=ListNode(t.val)
                    t1=t1.next
                    t=t.next
            else:
                t2=ListNode(t.val)
                j=t2
                t=t.next
                while t and t.val>=x:
                    t2.next=ListNode(t.val)
                    t2=t2.next
                    t=t.next
                    
        if not j and t:
            t2=ListNode(t.val)
            j=t2
            t=t.next
        elif not s and t:
            t1=ListNode(t.val)
            s=t1
            t=t.next
        
        while t:
            if t.val<x:
                t1.next=ListNode(t.val)
                t1=t1.next
                
            else:
                t2.next=ListNode(t.val)
                t2=t2.next
            t=t.next
        if t1:
            t1.next=j
            
        if s:
            return s
        else:
            return head     

        
        
        
        