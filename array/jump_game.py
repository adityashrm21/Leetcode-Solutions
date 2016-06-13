
        
class Solution(object):
    
    def canJump(self, nums):
        n=len(nums)
        cur=n-1
        
        for i in range(n-2,-1,-1):
            if i+nums[i]>=cur:
                cur=i
        return cur<=0
           
                
        