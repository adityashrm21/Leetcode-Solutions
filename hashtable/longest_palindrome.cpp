class Solution {
public:
    int longestPalindrome(string s) {
        
        int n=s.length();
        unordered_map<char, int> mp;
        
        for(int i=0;i<n;i++)
        {
            mp[s[i]]++;
        }
        
        int maxodd=0;
        char delval;
        
        for(auto it=mp.begin();it!=mp.end();it++)
        {
            if((it->second)%2!=0)
            {
                if(maxodd<(it->second));
                {
                    maxodd=it->second;
                    delval=it->first;
                }
                    
            }
            
        }
        mp.erase(delval);
        
        int ans=0;
        for(auto it=mp.begin();it!=mp.end();it++)
        {
            if((it->second)%2!=0)
            {
                ans+=(it->second)-1;
                
            }
            else ans+=(it->second);
        }
        return ans+maxodd;
        
    }
};