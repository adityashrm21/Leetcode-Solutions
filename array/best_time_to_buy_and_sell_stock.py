class Solution(object):
    def maxProfit(self, p):
        """
        :type p: List[int]
        :rtype: int
        """
        if len(p)<=1:
            return 0
            
        maxp=0
        
        minp=p[0]
        
        for i in range(len(p)):
            minp=min(minp,p[i])
            maxp=max(maxp,p[i]-minp)
        return maxp
            
