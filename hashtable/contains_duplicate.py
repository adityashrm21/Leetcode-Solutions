class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        d={}
        for i in range(n):
            if nums[i] in d:
                return True
                break
            d[nums[i]]=i
        
        return False
            