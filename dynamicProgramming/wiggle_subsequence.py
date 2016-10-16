class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp=[1]*(len(nums))
        
        if len(nums)<2:
            return len(nums)
        if len(nums)==2:
            if nums[0]!=nums[1]:
                return 2
            else: return 1
            
        j=1
        while j<len(nums) and nums[j]==nums[j-1]:
            dp[j]=dp[j-1]
            j+=1
        if j==len(nums): return dp[len(nums)-1]
        sign="+"
        if nums[j-1]-nums[j]>0:
            sign="+"
            dp[j]=dp[j-1]+1
            j+=1
        elif nums[j-1]-nums[j]<0:
            dp[j]=dp[j-1]+1
            sign="-"
            j+=1
        #print sign
        for i in range(j,len(nums)):
            #print i
            if sign=="-" and nums[i-1]-nums[i]>0:
                dp[i]=dp[i-1]+1
                sign="+"
                #print "yes", dp
                
            elif sign=="+" and nums[i-1]-nums[i]<0:
                dp[i]=dp[i-1]+1
                sign="-"
                
            else: 
                dp[i]=dp[i-1]
                #print dp[i], dp[i-1]
            #print dp
        #print dp
        n=len(nums)
        return dp[n-1]
        
        