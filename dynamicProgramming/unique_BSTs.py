class Solution(object):
    
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache=[-1]*(n+1)
        return self.countTrees(n,cache)
            
    def countTrees(self, n, cache):
        if n == 0:
            return 1
        if n == 1:
            return 1
     
        if cache[n]!=-1:
            return cache[n]
            
        Result = 0
        for i in xrange(n):
            LeftTrees = self.countTrees(i, cache)
            RightTrees = self.countTrees(n - i - 1, cache)
            Result += LeftTrees * RightTrees
        cache[n]=Result
        return Result    