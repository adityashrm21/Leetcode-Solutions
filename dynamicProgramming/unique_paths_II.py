class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        
        #ans=[[0]*n]*m
        ans = [[0]*n for _ in range(m)]
        if grid[0][0]==1 or grid[m-1][n-1]==1:
            return 0
        #print ans
        ans[0][0]=1
        #print ans
        
        for i in range(0,n):
            #print ans,i
            if grid[0][i]!=1:
                ans[0][i]=1
            else:
                break
        #print ans
        
        for i in range(0,m):
            #print ans,i
            if grid[i][0]!=1:
                ans[i][0]=1
            else: break
        
        #print ans 
        
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j]!=1:
                    ans[i][j]=ans[i-1][j]+ans[i][j-1]
        
       # print ans
        
        return ans[m-1][n-1]
        