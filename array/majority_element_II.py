class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ans=[]
        count=0
        for i in range(n):
            if len(ans)==0:
                if nums.count(nums[i])>n/3:
                    ans.append(nums[i])
                    count+=1
            if len(ans)==1:
                if ans[0]!=nums[i] and nums.count(nums[i])>n/3:
                    ans.append(nums[i])
                    count+=1
            
            if count==2:
                break
        
        return ans
        