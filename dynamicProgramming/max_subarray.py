class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        maxsofar=max(nums)
        temp=0
        for i in range(n):
            temp+=nums[i]
            if temp>=0:
                maxsofar=max(maxsofar, temp)
            else: temp=0
            
        return maxsofar