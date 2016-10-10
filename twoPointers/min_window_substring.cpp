class Solution {
public:
    string minWindow(string s, string t) {
        
        if(s.size()==0 || t.size()==0) return "";
        
        vector<int> rem(128,0);
        int req=t.size(), l=s.size();
        int i=0,start=0,left=0,minl=INT_MAX;
        
        for(int i=0;i<req;i++) rem[t[i]]++;
        
        while(i<=l && start<l)
        {
            if(req)
            {
                if(i==l) break;
                rem[s[i]]--;
                if(rem[s[i]]>=0)
                req--;
                i++;
            }
            else
            {
                if(i-start<minl)
                {
                    minl=i-start;
                    left=start;
                }
                rem[s[start]]++;
                if(rem[s[start]]>0)
                req++;
                start++;
            }
            
        }
        return minl==INT_MAX?"" :s.substr(left,minl);
    }
};