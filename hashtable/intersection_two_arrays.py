class Solution(object):
    def intersection(self, nums1, nums2):
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
            d1[nums1[i]]=nums1[i]
        
        for i in range(n):
            d2[nums2[i]]=nums2[i]
            
        if k==n:
            for i in range(k):
                if nums2[i] in d1:
                    ans.append(nums2[i])
        elif k==m:
            for i in range(k):
                if nums1[i] in d2:
                    ans.append(nums1[i])

        return list(set(ans))
                
            
                    