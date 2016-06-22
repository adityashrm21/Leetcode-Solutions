class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        arr=[]
        while 1: 
            s=0
            while n/10!=0:     
                temp=n%10
                s+=temp*temp
                n=n/10
            
            s+=n*n
            
            if s==1:
                return True
            else:
                print s
                if s not in arr:
                    arr.append(s)
                else: return False
                n=s
            
        