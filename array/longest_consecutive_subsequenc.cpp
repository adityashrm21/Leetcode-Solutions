class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        unordered_set<int> s;
        int n=nums.size(), ans=0;
        
        for(int i=0;i<n;i++)
        {
            s.insert(nums[i]);
        }
        for(int i=0;i<n;i++)
        {
            if(s.find(nums[i]-1)==s.end())
            {
                int j=nums[i], cur=0;
                while(s.find(j)!=s.end())
                {
                    cur++;
                    j++;
                }
                ans=max(ans,cur);
            }
        }
        return ans;
    }
};