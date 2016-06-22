class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n=len(nums)
        d={}
        for i in range(n):
            if nums[i] in d and abs(i-d[nums[i]])<=k:
                return True
                break
            d[nums[i]]=i
        
        return False
            