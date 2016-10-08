class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l=len(nums1) +len(nums2)
        
        if l%2!=0:
            return self.findkthsmallest(nums1, 0, nums2, 0, l/2+1)
        else:
            return (self.findkthsmallest(nums1, 0, nums2, 0, l/2)+self.findkthsmallest(nums1, 0, nums2, 0, l/2+1))/2.0
            
    def findkthsmallest(self, nums1, start1, nums2, start2, k):
        
        if start1>=len(nums1):
            return nums2[start2+k-1]
        if start2>=len(nums2):
            return nums1[start1+k-1]
        if k==1:
            return min(nums1[start1], nums2[start2])
        
        if start1+k/2-1<len(nums1):
            key1=nums1[start1+k/2-1]
        else:
            key1=99999
        if start2+k/2-1<len(nums2):
            key2=nums2[start2+k/2-1]
        else:
            key2=99999
            
            
        if key1<key2:
            return self.findkthsmallest(nums1, start1+k/2, nums2, start2, k-k/2)
        else:
            return self.findkthsmallest(nums1, start1, nums2, start2+k/2, k-k/2)
        
        
        
        
        
        
        
        
        