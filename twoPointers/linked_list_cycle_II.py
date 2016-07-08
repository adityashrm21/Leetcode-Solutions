# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast=head
        slow=head
        if not fast or not fast.next or not fast.next.next:
            return None
        while fast and fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                break

        temp=head
        while temp and slow and temp!=slow:
            temp=temp.next
            slow=slow.next
        
        if slow:
            return temp
        else: return None