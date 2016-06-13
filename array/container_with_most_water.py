class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area=0
        n=len(height)
        maxarea=0
        maxheight=0
        i=0
        j=n-1
        
        
        while i<j:
            maxheight=max(maxheight, height[i-1])
            area=min(height[i],height[j])*(j-i)
            maxarea=max(maxarea,area)
            
            if height[i]<height[j]:
                i+=1
            else: j-=1
        
        return maxarea