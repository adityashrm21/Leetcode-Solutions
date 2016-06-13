class Solution(object):
    def generateMatrix(self, n):
        
        if n==0:
            return []
        
        
        ans=[[0]*n for _ in range(n)]
        
        #print ans
        
        rowe=n-1
        rowb=0
        colb=0
        cole=n-1
        
        num=1
        
        #print ans[0][1]
        
        while rowb<=rowe and colb<=cole:
            for j in range (colb,cole+1):
                
                ans[rowb][j]=num
                #print rowb,j,ans[rowb][j]
                num+=1
            #print ans,1,num
            rowb+=1
            
            for i in range (rowb,rowe+1):
                
                ans[i][cole]=num
                #print i,cole,ans[i][cole]
                num+=1
            #print ans,2,num
            cole-=1
            
            if rowb<=rowe:
                for j in range (cole,colb-1,-1):
                    
                    ans[rowe][j]=num
                    #print rowe,j, ans[rowe][j]
                    num+=1
                #print ans,3,num
                #print ans
            rowe-=1
            #print rowe,"fff"
                    
            if colb<=cole:    
                for i in range (rowe,rowb-1,-1):
                    
                    ans[i][colb]=num
                    #print i,colb,ans[i][colb]
                    num+=1
                #print ans,4,num
            colb+=1
                
        
        return ans
                