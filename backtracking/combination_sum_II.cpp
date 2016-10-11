class Solution {
public:
    void getcomb(vector<int> &nums, vector<vector<int> > &ans, vector<int> &path, int n, int tar)
    {
        if(tar==0)
        ans.push_back(path);

        for(int i=n;i<nums.size() && tar>=nums[i];i++)
        {
            if(i==n || nums[i-1]!=nums[i])
            {
                path.push_back(nums[i]);
                getcomb(nums, ans, path, i+1, tar-nums[i]);
                path.pop_back();
        
                
            }
        }
        
    }
    
    vector<vector<int>> combinationSum2(vector<int>& nums, int tar) {
        int n=nums.size();
        sort(nums.begin(), nums.end());
        vector<vector<int> > ans;
        vector<int> path;
        getcomb(nums, ans, path,0, tar);
        return ans;
    }
};