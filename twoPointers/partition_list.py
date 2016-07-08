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
        temp=head
        temp1=None
        temp2=None
        join=None
        start=None
        
        if temp:
            if temp.val<x:
                temp1=ListNode(temp.val)
                temp=temp.next
                start=temp1
                while temp and temp.val<x:
                    #print "aaa"
                    temp1.next=ListNode(temp.val)
                    temp1=temp1.next
                    temp=temp.next
            else:
                temp2=ListNode(temp.val)
                temp=temp.next
                join=temp2
                while temp and temp.val>=x:
                    #print "bbb"
                    temp2.next=ListNode(temp.val)
                    temp2=temp2.next
                    temp=temp.next
                    
        #temp=temp.next
        
        if not join and temp:
            temp2=ListNode(temp.val)
            join=temp2
            temp=temp.next
        elif not start and temp:
            temp1=ListNode(temp.val)
            start=temp1
            temp=temp.next
        
        while temp:
            #print "fff"
            if temp.val<x:
                temp1.next=ListNode(temp.val)
                temp1=temp1.next
                
            else:
                temp2.next=ListNode(temp.val)
                temp2=temp2.next
            temp=temp.next
        if temp1:
            temp1.next=join
        
        if start:
            return start
        else: return head
        