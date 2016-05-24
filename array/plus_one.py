class Solution(object):
    def plusOne(self, d):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        j=len(d)-1
        
        
        if d[j]==9:
            while j>=0 and d[j]==9:
               # while d[j]==9:
                d[j]=0
                j-=1
                print j
                if j==-1:
                    d=[1]+d
                    return d

        d[j]+=1

            
        return d
        
