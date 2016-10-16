class Solution {
public:

   
    bool canPartition(vector<int>& nums) {
        
        int n=nums.size(), sum=0;
        
        for(int i=0;i<n;i++)
        sum+=nums[i];
        
        if(sum%2!=0) return false;
        
        int half=sum>>1;
        
        vector<bool>dp(half+1, false);
        
        dp[0]=true;
        
        
        for(auto num:nums)
        {
            for(int j=half;j>=num;j--)
            {
                if(dp[j-num])
                dp[j]=true;
            }
            
        }
        
       
        
        return dp[half];
        
        
    }
};