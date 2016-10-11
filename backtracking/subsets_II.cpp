class Solution {
public:
    void getsub(vector<int> &nums, vector<vector<int> > &ans, vector<int> &path, int n)
    {
        ans.push_back(path);
        
        for(int i=n;i!=nums.size();++i)
        {
            if(i==n || nums[i]!=nums[i-1])
            {
                path.push_back(nums[i]);
                getsub(nums, ans, path, i+1);
                path.pop_back();
            }
        }
        
    }
    
    vector<vector<int>> subsetsWithDup(vector<int>& nums)
    {
        sort(nums.begin(), nums.end());
        //int n=nums.size();
        vector<vector<int> > ans;
        vector<int> path;
        getsub(nums, ans, path,0);
        return ans;
    }

};
