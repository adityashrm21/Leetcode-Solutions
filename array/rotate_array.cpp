class Solution {
public:

    void rotate(vector<int>& nums, int k) {
        
        int n=nums.size(), z;
        
        k%=n;
        
        for( int i=0;i<k;i++)
        {
            int temp=nums[n-1];
            nums.erase(nums.end()-1);
            nums.insert(nums.begin(),temp);
        
        }
        
    }
};