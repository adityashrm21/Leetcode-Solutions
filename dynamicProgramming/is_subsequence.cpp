class Solution {
public:
    bool isSubsequence(string s, string t) 
    {
        int n=s.size(), m=t.size();
        if(n==0) return true;
        if(m==0) return false;
        
        int targ=0;
        
        
        for(int i=0;i<m;i++)
        {
        
            if(t[i]==s[targ])
            {
                if(targ==n-1) return true;
                targ++;
            }
        }
        return false;
        
       
      
    }
};