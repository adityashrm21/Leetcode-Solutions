class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=[0]*n
        ans[0]=1
        if n==1:
            return ans[0]
        ans[1]=2
        if n<3:
            return ans[n-1]
            
        for i in range(2,n):
            ans[i]=ans[i-1]+ans[i-2]
            
        return ans[n-1]