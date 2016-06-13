class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if len(matrix)==0:
            return []
            
        rowe=len(matrix)-1
        rowb=0
        colb=0
        cole=len(matrix[0])-1
        
        
        ans=[]
        
        
        while rowb<=rowe and colb<=cole:
            for j in range (colb,cole+1):
                ans.append(matrix[rowb][j])
            rowb+=1
            
            for i in range (rowb,rowe+1):
                ans.append(matrix[i][cole])
            cole-=1
            
            if rowb<=rowe:
                for j in range (cole,colb-1,-1):
                    ans.append(matrix[rowe][j])
            rowe-=1
                    
            if colb<=cole:    
                for i in range (rowe,rowb-1,-1):
                    ans.append(matrix[i][colb])
            colb+=1
                
        
        return ans
                