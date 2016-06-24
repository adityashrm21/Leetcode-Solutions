# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ta=headA
        tb=headB
        while ta and tb:
            ta=ta.next
            tb=tb.next
            
        if tb:
            while tb:
                headB=headB.next
                tb=tb.next
        if ta:
            while ta:
                headA=headA.next
                ta=ta.next
                
        while headA and headB:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        
        return None
            