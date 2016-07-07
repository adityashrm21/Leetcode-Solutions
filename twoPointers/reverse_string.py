class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        arr=[]
        i=0
        j=n-1

        for x in range(n):
            arr.append(s[x])
        
        while i<j:

            arr[i],arr[j]=arr[j],arr[i]
            
            i+=1
            j-=1
        
        ans=""
        for i in range(n):
            ans+=str(arr[i])
            
        return ans