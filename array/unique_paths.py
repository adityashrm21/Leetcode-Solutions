class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans=[[0]*n]*m
        ans[0][0]=1
        for i in range(1,n):
            ans[0][i]=1
        for i in range(1,m):
            ans[i][0]=1
        print ans 
        
        for i in range(1,m):
            for j in range(1,n):
                ans[i][j]=ans[i-1][j]+ans[i][j-1]
        
        return ans[m-1][n-1]