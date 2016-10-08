class Solution {
public:
    char findTheDifference(string s, string t) {
        
        int n=s.size(), m=t.size();
        
        unordered_map<char,int> mp;
        
        for(int i=0;i<m;i++)
        {
            mp[t[i]]++;
        }
        
        int i;
        for(i=0;i<n;i++)
        {
            mp[s[i]]--;
        }
        
        for(auto it=mp.begin();it!=mp.end();it++)
        {
            if(it->second>0)
            return it->first;
        }
        return t[i];//doesn't matter
    }
};