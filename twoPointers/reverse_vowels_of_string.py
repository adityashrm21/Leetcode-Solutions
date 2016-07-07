class Solution(object):
    def reverseVowels(self, s):
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
            while i<j and arr[i]!='a' and arr[i]!='e' and arr[i]!='i' and arr[i]!='o' and arr[i]!='u' and arr[i]!='A' and arr[i]!='E' and arr[i]!='I' and arr[i]!='O' and arr[i]!='U':
                i+=1

            while i<j and arr[j]!='a' and arr[j]!='e' and arr[j]!='i' and arr[j]!='o' and arr[j]!='u' and arr[j]!='A' and arr[j]!='E' and arr[j]!='I' and arr[j]!='O' and arr[j]!='U':
                j-=1

            if i>=j:
                break
            

            arr[i],arr[j]=arr[j],arr[i]
            
            i+=1
            j-=1
        
        ans=""
        for i in range(n):
            ans+=str(arr[i])
            
        return ans
            