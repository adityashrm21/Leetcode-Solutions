class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        n=len(nums)
        
        d={}
        ans=[]
        for i in range(n):
            d[nums[i]]=i
            print d[nums[i]]
       
        for i in range(n):
            tar=target-nums[i]
            #print tar
            if tar in d and d[tar]!=i:
                #print 4
                ans.append(i)
                ans.append(d[tar])
                break
            
        return ans