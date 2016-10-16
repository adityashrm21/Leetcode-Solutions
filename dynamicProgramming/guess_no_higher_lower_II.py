class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[[0]*(n+1) for i in xrange(n+1)]
        
        for lo in xrange(n,0,-1):
            for hi in xrange(lo+1,n+1):
                dp[lo][hi]=min(i+max(dp[lo][i-1], dp[i+1][hi]) for i in xrange(lo,hi))
        
        return dp[1][n]
        
        