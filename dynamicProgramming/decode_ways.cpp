class Solution {
public:
    int numDecodings(string s) {
        
        int n=s.size();
        if(n==0 || s[0]=='0') return 0;
        
        int cur=0, p=1, p2=1;
        
        for(int i=1;i<=n;i++)
        {
            cur=0;
            if(s[i-1]!='0') cur+=p;

            
            if(i>=2)
            {
                int comp=stoi(s.substr(i-2,2));
                if(comp>=10 && comp<27)
                {
                    cur+=p2;
                    
                }
                p2=p;
            }
            p=cur;
        }
        return cur;
       
    }
};