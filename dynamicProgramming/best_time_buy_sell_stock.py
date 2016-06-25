class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        
        if n<2:
            return 0
        mintillnow=prices[0]
        ans=max(prices[1]-prices[0],0)
        for i in range(2,n):
            mintillnow=min(prices[i-1],mintillnow)
            if prices[i]-mintillnow>=ans:
                ans=prices[i]-mintillnow
        
        return ans
        