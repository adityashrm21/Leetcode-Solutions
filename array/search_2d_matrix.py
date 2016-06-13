class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n=len(matrix)
        m=len(matrix[0])
        
        #for i in range(n):
        i=0    
        while matrix[i][m-1]<target:
            i+=1
            if i>=n:
                return False
        #i-=1
            
        if i<n:
            for j in matrix[i]:
                if j==target:
                    return True
        
        return False
                