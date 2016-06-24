# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        temp=head
        prev=None
        
        while temp and temp.val==val:
            temp=temp.next
            prev=temp
            head=prev
        
        while temp and temp.next:
            prev=temp
            temp=temp.next
            while temp and temp.val==val:
                temp=temp.next
            prev.next=temp
            prev=temp
        return head
        