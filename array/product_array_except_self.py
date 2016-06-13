class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[1]*len(nums)
        n=len(nums)
        
        prod=1
        for i in range(1,n):
            prod=prod*nums[i-1]
            output[i]*=prod
            
        prod=1
        for i in range(n-2,-1,-1):
            prod=prod*nums[i+1]
            output[i]*=prod
        
        return output
            