class Solution(object):
    def generate(self, numRows):
    
        if numRows<=0:
            return []
        ans=[]
        #ans.append([1])
        
        for i in range(numRows):
            temp=[]
            #print temp
            for j in range(i+1):
                if j==0 or j==i:
                    temp.append(1)
                else: 
                    temp.append(ans[i-1][j-1]+ans[i-1][j])
        
            ans.append(temp)
            
        return ans
