class Solution(object):
    def minimumTotal(self, tri):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        n=len(tri)
        su=[]
        su[:]=tri[n-1][:]

        minsofar=0
    
        for i in range(n-2,-1,-1):
          
            for j in range(0,i+1):
    
                print tri[i][j], min(tri[i+1][j], tri[i+1][j+1])
                su[j]=tri[i][j]+min(su[j],su[j+1])

        return su[0]
        