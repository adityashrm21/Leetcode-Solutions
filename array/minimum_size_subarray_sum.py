class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        r=len(nums)-1
        l=0
        minlen=r+2
        sum=0
        
        for r in range(r+1):
            sum+=nums[r]
            while sum>=s:
                minlen=min(minlen,r-l+1)
                sum-=nums[l]
                l+=1
        
        if minlen>len(nums):
            return 0
        else: return minlen