class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if not nums:
            return 0
        if n<3:
            return max(nums)
        dp=[0]*n
        dp[0]=nums[0]
        #dp[1]=nums[1]
        ans=0
        for i in range(1,n):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
            #ans=max(dp)
        return dp[n-1]
        