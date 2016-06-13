class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        nums.sort()
        
        self.combs(nums,0,[],ans)
        ans =[tuple(a) for a in ans]
        
        return list(set(ans))
        
    def combs(self, nums, index, path, ans):

        ans.append(path)
        for i in range(index, len(nums)):
            
            self.combs(nums, i+1, path+[nums[i]], ans)