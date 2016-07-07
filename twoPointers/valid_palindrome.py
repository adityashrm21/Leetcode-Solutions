class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        
        n=len(s)
        a=[]
        for i in range(n):
            if str(s[i]).isalnum():
                a.append(s[i])
        
        print a
        
        i=0
        j=len(a)-1
        
        while i<=j:
            if a[i]==a[j]:
                i+=1
                j-=1
            else:
                return False
        return True
        