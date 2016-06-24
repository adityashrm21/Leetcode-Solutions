# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
            
        if not l1:
            return l2
        if not l2:
            return l1
            
        temp1=l1
        temp2=l2
        
        if temp1.val<temp2.val:
            while temp1 and temp2:
    
                while temp1 and temp2 and temp1.val<=temp2.val:
                    prev= temp1
                    temp1=temp1.next
                    #print "xxx"
                prev.next=temp2
                while temp1 and temp2 and temp2.val<=temp1.val:
                    prev=temp2
                    temp2=temp2.next
                    #print "yyy"
                prev.next=temp1
            if temp2:
                prev.next=temp2
            if temp1:
                prev.next=temp1
            return l1
            
        else:
            while temp1 and temp2:
            
                while temp1 and temp2 and temp2.val<=temp1.val:
                    prev= temp2
                    temp2=temp2.next
                    
                prev.next=temp1
                while temp1 and temp2 and temp1.val<=temp2.val:
                    prev=temp1
                    temp1=temp1.next
                prev.next=temp2
            if temp2:
                prev.next=temp2
            if temp1:
                prev.next=temp1                
            return l2
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    