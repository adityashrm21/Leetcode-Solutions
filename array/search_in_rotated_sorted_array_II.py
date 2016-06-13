class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n=len(nums)
        
        for i in range(n):
            if nums[i]==target:
                return True
        
        return False
                
        