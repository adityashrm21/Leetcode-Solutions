class Solution(object):
    def removeDuplicates(self, nums):
        n=len(nums)
        if not nums:
            return 0
        i=0
        j=1
        while j<n:
            if nums[i]!=nums[j]:
                nums[i+1],nums[j]=nums[j],nums[i+1]
                j+=1
                i+=1
            else: j+=1
        return i+1
            

