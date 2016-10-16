class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        nums.sort()
        if(n==0):
            return []
        
        maxlen=0
        maxind=0
        prev=[-1]*n
        
        dp=[1]*n
        
        for i in range(n):
            for j in range(i-1,-1,-1):
                if nums[i]%nums[j]==0 and dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
                    prev[i]=j
            
            if dp[i]>maxlen:
                maxlen=dp[i]
                maxind=i
        
        ans=[]
        
        while maxind>=0:
            ans.append(nums[maxind])
            maxind=prev[maxind]
        #ans.sort()
        
        return ans