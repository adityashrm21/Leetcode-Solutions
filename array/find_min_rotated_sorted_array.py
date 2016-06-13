class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=nums[0]
        
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                ans=nums[i]
                break
        return ans