class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n=len(nums)
        
        if n==0:
            return []
        if n==1:
            return [str(nums[0])]
            
        ans=[]
        #start=nums[0]
        #end=nums[0]
        i=0
        
        while i<n:
            start=nums[i]
            print start
            if i<n-1:    
                while i<n-1 and nums[i]==nums[i+1]-1:
                    i+=1
                
            #if start==nums[i]:    
            end=nums[i]
            #else: end=nums[i-1]
            
            if start==end:
                ans.append(str(start))
            
            elif start!=end:
                ans.append(str(start)+"->"+str(end))
            
            i+=1
            

        
        return ans
        