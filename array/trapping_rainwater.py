class Solution(object):
    def trap(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(h)
        #print n
        l=0
        r=n-1
        area=0
        minh=0
        while l<r:
            while l<r and h[l]<=minh:
                area+=minh-h[l]
                l+=1
            while l<r and h[r]<=minh:
                area+=minh-h[r]
                r-=1
            minh=min(h[l],h[r])
        return area
            
                    