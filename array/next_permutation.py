class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        i=len(nums)-1
        n=len(nums)
        
        while i>0 and nums[i-1]>=nums[i]: 
            i-=1
        if i!=0:
            j=n-1
            m=nums[i-1]
            ind=0
            print i
            while j>=i and nums[j]<=nums[i-1]:
                    j-=1
                #print j

            #print ind
            #print nums
            print i-1, ind
                
            nums[i-1],nums[j]=nums[j],nums[i-1]
            #print nums
            
            k=n-1
            while i<=k:
                nums[i],nums[k]=nums[k],nums[i]
                i+=1
                k-=1
        else:
            k=n-1
            i=0
            while i<=k:
                nums[i],nums[k]=nums[k],nums[i]
                i+=1
                k-=1
                