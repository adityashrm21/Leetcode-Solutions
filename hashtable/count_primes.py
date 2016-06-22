class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 0 
        primes=[True]*n
        primes[0]=primes[1]=False
        for i in xrange(2,n):
            if primes[i]:
                primes[i*i:n:i]=[False]*len(primes[i*i:n:i])
        return sum(primes)    
            