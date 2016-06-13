class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        n=len(candidates)
        
        self.combs(candidates,0,[],target,ans)
        
        return ans
        
    def combs(self, nums, index, path, target, ans):
        
        if target<0:
            return
        if target==0:
            ans.append(path)
            return
        
        for i in range(index, len(nums)):
            self.combs(nums, i, path+[nums[i]], target-nums[i], ans)