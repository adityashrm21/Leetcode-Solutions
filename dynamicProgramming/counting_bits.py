class Solution(object):
    def countBits(self, n):
        """
        :type num: int
        :rtype: List[int]
        """
        if n==1:
            return [0,1]
        ans=[0,1]
        e=1
        i=0
        x=2
    
        while x<=n:
            for i in xrange(pow(2,e), pow(2,e+1)-1):
                ans.append(ans[x-pow(2,e)]+1)
                x+=1
            e+=1
            print x

        return ans[0:n+1]