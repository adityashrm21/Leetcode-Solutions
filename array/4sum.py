class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        
        for l in range(0,len(nums)-3):
            for m in range(l+1,len(nums)-2):
                i=m+1
                r=len(nums)-1
                while i<r and i>m:
                    sum=nums[l]+nums[r]+nums[i]+nums[m]        
                    if sum==target:
                        a=[nums[l],nums[m],nums[i],nums[r]]
                        ans.append(a)
                        i+=1
                    elif sum>target:
                        r-=1
                    else: 
                        i+=1
                    
        ans = set(map(tuple, ans))
        return list(ans)