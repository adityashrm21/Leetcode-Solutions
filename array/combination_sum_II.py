class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        candidates.sort()
        
        self.combs(candidates,0,[],target,ans)
        
        return ans
        
    def combs(self, nums, index, path, target, ans):
        
        #if target<0:
         #   return
        if target==0:
            ans.append(path)
            return

        
        
        for i in range(index, len(nums)):
            if nums[i]>target:
                break
            if i>index and nums[i]==nums[i-1]:
                continue
            
            self.combs(nums, i+1, path+[nums[i]], target-nums[i], ans)