class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        f=[0]*(n+1)
        if n==0:
            return 1
        f[1]=10
        if n==1:
            return 10
        f[2]=9*9+f[1]
        
        for i in range(2, n):
            temp=9*9
            j=1
            while j<i:
                temp*=(9-j)
                print j
                j+=1
            f[i+1]=temp

            
        for i in range(3,n+1):
                f[i]+=f[i-1]
                
        return f[n]