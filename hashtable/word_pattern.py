class Solution(object):
    def wordPattern(self, pat, st):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ds={}
        dt={}
        m=len(pat)
        st=list(st.split())
        n=len(st)
        if m!=n:
            return False
   
        for i in range(m):
            if pat[i] in ds and st[i] in dt:
                if pat[i]!=dt[st[i]] or st[i]!=ds[pat[i]]:    
                    return False
            elif pat[i] in ds and st[i] not in dt:
                return False
            elif pat[i] not in ds and st[i] in dt:
                return False
            
            else: 
                ds[pat[i]]=st[i]
                dt[st[i]]=pat[i]
        return True
            