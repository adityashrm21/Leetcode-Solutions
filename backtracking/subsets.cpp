class Solution {
public:

    void getsub(vector<int> &nums, vector<vector<int> > &ans, vector<int> &path, int n)
    {

        ans.push_back(path);
        
        for(int i=n;i>=0;i--)
        {
            path.push_back(nums[i]);
            getsub(nums, ans, path, i-1);
            path.pop_back();
        }
        
    }
    
    vector<vector<int>> subsets(vector<int>& nums) 
    {
        int n=nums.size();
        vector<vector<int> > ans;
        vector<int> path;
        getsub(nums, ans, path,n-1);
        return ans;
    }
};