class Solution(object):
    def largestRectangleArea(self, h):
        """
        :type heights: List[int]
        :rtype: int
        """
        s=[]
        n=len(h)
        ans=0
        i=0
        while i<n:
            if len(s)==0 or h[i]>=h[s[-1]]:
                s.append(i)
                i+=1
            else:
                t=s[-1]
                s.pop()
                if len(s)==0:
                    k=i
                else: k=i-s[-1]-1
                area=h[t]*k
                ans=max(ans,area)
        while len(s)>0:
            t=s[-1]
            s.pop()
            if len(s)==0:
                k=i
            else: k=i-s[-1]-1
            area=h[t]*k
            ans=max(ans,area)
            
        return ans
        