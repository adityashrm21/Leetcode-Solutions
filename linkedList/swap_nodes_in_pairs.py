# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp1=temp2=temp3=head
        if not head or not head.next:
            return head
        if head.next:
            head=head.next
           
        temp2=temp1.next
        temp3=temp1.next.next
        #prev.next=temp2
        temp2.next=temp1
        temp1.next=temp3
        prev=temp1
        temp1=temp3
        
        while temp1 and temp1.next and temp1.next.next:
            temp2=temp1.next
            temp3=temp1.next.next
            prev.next=temp2
            temp2.next=temp1
            temp1.next=temp3
            prev=temp1
            temp1=temp3
            
        if temp1 and temp1.next:
            temp2=temp1.next
            prev.next=temp2
            temp2.next=temp1
            temp1.next=None
        
        return head
            
            
            
            