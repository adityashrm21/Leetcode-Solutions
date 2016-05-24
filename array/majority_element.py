#from collections import Counter
class Solution(object):
    
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in set(nums):
            if nums.count(i)>len(nums)/2:
                return i
