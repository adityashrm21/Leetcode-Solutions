class Solution(object):
    def isIsomorphic(self, s, t):

        ds={}
        dt={}
        m=len(s)
        n=len(t)
        if m!=n:
            return False
   
        for i in range(m):
            #if ds[s[i]]!=0 and dt[t[i]]!=0:
            if s[i] in ds and t[i] in dt:
                if s[i]!=dt[t[i]] or t[i]!=ds[s[i]]:    
                    return False
            elif s[i] in ds and t[i] not in dt:
                return False
            elif s[i] not in ds and t[i] in dt:
                return False
            
            else: 
                ds[s[i]]=t[i]
                dt[t[i]]=s[i]
        return True
