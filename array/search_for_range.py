class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        r=n-1
        l=0
        ans=[99999,-1]
        #print 'fff'
        while l<=r:
            #print 'ff'
            mid=(r+l)/2
            if nums[mid]==target:
                ans[0]=mid
                r-=1
                #print 'fff'
            elif nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
        
        
        r=n-1
        l=0
       
        while l<=r:
            #print 'f'
            mid=(r+l)/2
            if nums[mid]==target:
                ans[1]=mid
                l+=1
                #print 'fff'
            elif nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            
        if ans[0]==99999:
            ans[0]=-1
        return ans
        