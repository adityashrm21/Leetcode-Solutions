class Solution(object):
    def isValidSudoku(self, bd):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        d={}
        for j in range(9):
            for i in range(9):
                d[bd[j][i]]=0
            for i in range(9):
                d[bd[j][i]]+=1
                if d[bd[j][i]]>1 and bd[j][i]!=".":
                    #print bd[j][i], d[bd[j][i]], "first"
                    return False
            d.clear()
            
        for j in range(9): 
            for i in range(9):
                d[bd[i][j]]=0
            for i in range(9):
                d[bd[i][j]]+=1
                if d[bd[i][j]]>1 and bd[i][j]!=".":
                    #print bd[i][j], d[bd[i][j]], "second"
                    return False
            d.clear()
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        d[bd[k][l]]=0
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        d[bd[k][l]]+=1
                        if bd[k][l]!="." and d[bd[k][l]]>1:
                            #print bd[k][l], d[bd[k][l]], "third"
                            return False
                d.clear()
            
            
        return True
            
            
            