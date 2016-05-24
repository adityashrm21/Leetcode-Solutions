class Solution(object):
    def getRow(self, numRows):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        ans=[]
        #ans.append([1])
        
        for i in range(numRows+1):
            temp=[]
            #print temp
            for j in range(i+1):
                if j==0 or j==i:
                    temp.append(1)
                else: 
                    temp.append(ans[i-1][j-1]+ans[i-1][j])
        
            ans.append(temp)
            
        return ans[numRows]
        
