class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l=len(nums)-1
        i=0
            
        while i<=l:
            if nums[i]==val:
                nums[i],nums[l]=nums[l],nums[i]
                l-=1
            
            else: i+=1
            
        return l+1
                
        
