class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        ds={}
        dg={}
        m=len(secret)
        for i in xrange(m):
            ds[secret[i]]=0
            dg[guess[i]]=0
        
        bulls=0
        cows=0
        
        for i in xrange(m):
            ds[secret[i]]+=1
            dg[guess[i]]+=1
            
            if secret[i]==guess[i]:
                bulls+=1
                ds[secret[i]]-=1
                dg[guess[i]]-=1
                
            elif guess[i] in ds and ds[guess[i]]>0:
                cows+=1
                #print i,guess[i], ds[guess[i]]
                dg[guess[i]]-=1
                ds[guess[i]]-=1
            #else:
             #   dg[guess[i]]-=1
              #  ds[secret[i]]-=1
        print ds, dg, cows
              
        for i in xrange(m):
            if guess[i] in ds and ds[guess[i]]>0 and dg[guess[i]]>0:
                cows+=1
                #print i,guess[i], ds[guess[i]]
                dg[guess[i]]-=1
                ds[guess[i]]-=1
        
                
        return str(bulls)+"A"+str(cows)+"B"
            