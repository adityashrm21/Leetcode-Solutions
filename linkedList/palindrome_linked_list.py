# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast=head
        slow=head
        if not head or not head.next:
            return True

        while fast and fast.next and fast.next.next:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        
        if fast.next:
            temp1=slow
            temp2=slow.next
            temp1.next=None
        else:
            temp1=prev
            temp2=slow.next
            temp1.next=None
    
        prev=None
        cur=head
        #nex=head.next
        
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        
        while prev and temp2:
            if prev.val==temp2.val:
                temp2=temp2.next
                prev=prev.next
            else: return False
        return True