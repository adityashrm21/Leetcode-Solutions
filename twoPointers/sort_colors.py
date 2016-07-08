class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        l=0
        mid=0
        r=len(nums)-1
     
        while l<=r:
            
            if nums[l]==2:
                nums[l],nums[r],=nums[r],nums[l]
                r-=1
                #mid+=1

            elif nums[l]==0:
                nums[l],nums[mid]=nums[mid],nums[l]
                l+=1
                mid+=1
            else: 
                l+=1
                #mid+=1
     
            
            
            
            