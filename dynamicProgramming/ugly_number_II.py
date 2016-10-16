class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==0:
            return 0
            
        ans=[0]*(n)
        i2=0
        i3=0
        i5=0
        ans[0]=1
        for i in range(1,n):
            ##print l1[j-3:j]
            ans[i]=min([2*ans[i2],3*ans[i3], 5*ans[i5]])
            if ans[i]==2*ans[i2]:
                i2+=1
            if ans[i]==3*ans[i3]:
                i3+=1
            if ans[i]==5*ans[i5]:
                i5+=1
            
        #print ans
        return ans[n-1]