class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)==len(set(nums)):
            return False
        d={}   
        for i,val in enumerate(nums):
            if val in d and i-d[val]<=k:
                return True
            else: d[val]=i
            
        return False
        
