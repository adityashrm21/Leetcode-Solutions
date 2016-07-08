class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        
        i=0
        if n>1:
            j=1
        else:
            return n
        ans=1
        count=1
        d={}
        for k in range(n):
            d[s[k]]=-1
        k=0
        d[s[i]]=i
        while i<=j and j<n:
            if d[s[j]]==-1:
                d[s[j]]=j
                count+=1
                ans=max(ans,count)
#                j+=1
            else:
                
                count-=(d[s[j]]-i)
                i=d[s[j]]+1
                for o in range(k,i):
                    if s[o] not in s[i:j+1]:
                        d[s[o]]=-1
                k=o
                d[s[j]]=j

            j+=1
        return ans
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                