class Solution {
public:
    int maxProduct(vector<int>& arr) 
    {
        int n=arr.size();
        vector<int> dp(n,1), dn(n,1);
        if(n==1) return arr[0];
        //dp[0]=nums[0];
        //dn[0]=nums[0];
        int maxpos=0, minpos=0;
        int ans=0;
        for(int i=0;i<n;i++)
        {
            if(arr[i]<0)
            {
                swap(minpos, maxpos);
            }
            maxpos=max(maxpos*arr[i],arr[i]);
            minpos=min(minpos*arr[i],arr[i]);
            ans=max(ans, maxpos);
        }
        
        return ans;
    }
};