class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        mtn=99999
        minsum=99999
        ans=[]
        for l in range(0,len(nums)-2):
            i=l+1
            r=len(nums)-1
            while i<r and i>l:
                s=nums[l]+nums[r]+nums[i]        
                if abs(s-target)==0:
                    return s
                elif (s-target)>0:
                    r-=1
                    mtn=min(mtn,abs(s-target))
                    if mtn==abs(s-target):
                        minsum=s
                    
                else: 
                    i+=1
                    mtn=min(mtn,abs(s-target))
                    if mtn==abs(s-target):
                        minsum=s
                    
        return minsum