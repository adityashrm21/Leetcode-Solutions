class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans=[]
        n=len(s)
        for i in [1,2,3]:
            for j in [i+1,i+2,i+3]:
                for k in [j+1,j+2,j+3]:
                    if k>=n:
                        continue
                    else:
                        s1=s[:i]
                        s2=s[i:j]
                        s3=s[j:k]
                        s4=s[k:]
                        
                        if self.isvalid([s1,s2,s3,s4]):
                            ans.append(s1+"."+s2+"."+s3+"."+s4)
        return ans
        
        
    def isvalid(self, slist):
        
        for s in slist:
            if s[0]=="0" and s!="0":
                return False
            if int(s)>255:
                return False
        return True
        
        
        