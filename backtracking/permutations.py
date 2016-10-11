class Solution(object):
    
    
    def perm(self,A,ans,path):
        if not A:
            #print A
            ans.append(path)
            return

            
        for i, num in enumerate(A):
            self.perm(A[:i]+A[i+1:], ans,path+[num])
            
    def permute(self, A):
        ans=[]
        self.perm(A,ans,[])
        return ans
        