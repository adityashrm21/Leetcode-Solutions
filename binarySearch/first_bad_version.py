# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=1
        high=n
        
        while low<=high:
            mid=(low+high)/2
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid) and isBadVersion(mid-1):
                high=mid-1
            elif not isBadVersion(mid) and isBadVersion(mid+1):
                return mid+1
            elif not isBadVersion(mid) and not isBadVersion(mid-1):
                low=mid+1
            

            
        
        