class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m=len(nums1)
        n=len(nums2)
        nums1.sort()
        nums2.sort()
        
        k=min(m,n)
        ans=[]
        
        d1={}
        d2={}
        
        for i in range(m):
            d1[nums1[i]]=0
        
        for i in range(n):
            d2[nums2[i]]=0
        
        
        for i in range(m):
            d1[nums1[i]]+=1
        
        for i in range(n):
            d2[nums2[i]]+=1
        
        for i in d1:
            if i in d2:
                for j in range(min(d1[i],d2[i])):
                    ans.append(i)
                    #print i
        
        return ans
                