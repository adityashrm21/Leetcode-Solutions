class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        for l in range(0,len(nums)-2):
            i=l+1
            r=len(nums)-1
            while i<r and i>l:
                sum=nums[l]+nums[r]+nums[i]        
                if sum==0:
                    a=[nums[l],nums[i],nums[r]]
                    ans.append(a)
                    i+=1
                elif sum>0:
                    r-=1
                else: 
                    #l+=1
                    i+=1
                    
        ans = set(map(tuple, ans))
        return list(ans)