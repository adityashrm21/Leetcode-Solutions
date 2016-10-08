class Solution {
public:
    int jump(vector<int>& nums) {
        
        int n=nums.size();
        
        int reach(0), nextr(-1), count(0);
        
        for(int i=0;i<n-1 && i<=reach;i++)
        {
            nextr=max(nextr, i+nums[i]);
            if(i==reach)
            {
                ++count;
                reach=nextr;
            }
           
        }
        return reach>=n-1?count:INT_MAX;
        
    }
};