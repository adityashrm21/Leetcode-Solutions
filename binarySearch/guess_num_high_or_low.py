# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=1
        high=n
        while True:
            mid=(high-low)/2+low
            if guess(mid)==0:
                return mid
            elif guess(mid)==-1:
                high=mid-1
            else: low=mid+1