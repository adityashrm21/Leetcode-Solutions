class Solution(object):
    def maxProfit(self, p):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(p)<=1:
            return 0
            
        maxp=p[1]
        n=len(p)
        minp=p[0]
        profit=0
        i=1
        if n==2 and p[1]>p[0]:
            return p[1]-p[0]
            
        while i<n-1:
            #print i
            while i<n-1 and p[i]<p[i+1]:
                    
                maxp=p[i+1]
                minp=min(minp,p[i])
                i+=1
            
            if maxp>minp:
                profit+=maxp-minp
            #print profit
            
            if i<n-1:        
                minp=p[i+1]
                maxp=p[i+1]
            
            i+=1
            #print i
            #maxp=max(maxp,p[i+2]) 
            
            '''
                maxp=max(maxp,p[i+1])
                minp=min(minp,p[i])
            else:
                profit+=maxp-minp
                #minp=min(minp,p[i])
                maxp=p[i+1]
                minp=p[i+1]
                #maxp'''
                
        return profit
            