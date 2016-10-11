class Solution {
public:
    void getcomb(vector<int> &nums, vector<vector<int> > &ans, vector<int> &path, int n, int tar)
    {
        if(tar==0)
        ans.push_back(path);

        for(int i=0;i<=n;i++)
        {
            path.push_back(nums[i]);
            if(tar-nums[i]>=0)
            getcomb(nums, ans, path, i, tar-nums[i]);
            path.pop_back();
        }
        
    }
    
    vector<vector<int>> combinationSum(vector<int>& nums, int tar) {
        int n=nums.size();
        vector<vector<int> > ans;
        vector<int> path;
        getcomb(nums, ans, path,n-1, tar);
        return ans;
    }
};