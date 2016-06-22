class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        n=len(s)
        m=len(t)
        ds={}
        dt={}
        if m!=n:
            return False
        
        for i in range(m):
            dt[t[i]]=0
        for i in range(m):
            dt[t[i]]+=1
        print dt  
        for i in range(n):
            if s[i] in dt:
                dt[s[i]]-=1
                
        for i in range(n):
            if dt[t[i]]!=0:
                return False
                
        return True