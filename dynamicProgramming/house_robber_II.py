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
            
        dp1=[0]*(n)
        dp2=[0]*(n)
        
        val=nums[n-1]
        
        dp1[1]=nums[0]

        nums=nums[:n-1]
        
        for i in range(2,n):
            dp1[i]=max(dp1[i-2]+nums[i-1],dp1[i-1])

        
        nums=nums[1:n-1]
        nums=nums+[val]
        
        dp2[1]=nums[0]


        for i in range(2,n):
            dp2[i]=max(dp2[i-2]+nums[i-1],dp2[i-1])
        
        return max(dp1[n-1], dp2[n-1])
        