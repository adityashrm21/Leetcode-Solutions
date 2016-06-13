class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        prod=nums[0]
        
        if n==1:
            return nums[0]
        maxmod=0
        minmod=0
        
        for i in range(n):
            if nums[i]<0:
                maxmod,minmod=minmod,maxmod
            minmod=min(nums[i], minmod*nums[i])
            
            maxmod=max(nums[i], maxmod*nums[i])
        
            
            prod=max(prod,maxmod)
            
        return prod