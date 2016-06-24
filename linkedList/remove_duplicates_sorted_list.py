# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp=head
        prev=head
        
        while temp:
            while temp.next and temp.val==temp.next.val:
                temp=temp.next
            prev.next=temp.next
            temp=temp.next
            prev=prev.next
        
        return head