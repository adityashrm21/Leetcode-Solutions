class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> ans;
        
        int l=s.size(), n=words.size();
        if(l==0) return ans;
        
        int i=0,wsize=words[0].size();
        
        unordered_map<string, int> count;
        
        for(int i=0;i<n;i++)
        {
            count[words[i]]++;
        }
        
        for( int i=0;i<l-n*wsize+1;i++)
        {
            unordered_map<string,int> seen;
            int j=0;
            
            while(j<n)
            {
                string sub=s.substr(i+j*wsize, wsize);
                if(count.find(sub)!=count.end())
                {
                    seen[sub]++;
                    if(seen[sub]>count[sub])
                    break;
                }
                else break;
                j++;
                if(j==n)
                ans.push_back(i);
            }
        }
        return ans;

    }
};