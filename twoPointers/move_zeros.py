class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        j=0
        i=0
        while j<len(nums):
            print j,i
            if nums[j]!=0:
                nums[i],nums[j]=nums[j], nums[i]
                i+=1
                j+=1
            else:
                j+=1
        
