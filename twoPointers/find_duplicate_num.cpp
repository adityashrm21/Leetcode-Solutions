class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
        int slow=nums[0], fast=nums[nums[0]];
        
        while(fast!=slow)
        {
            slow=nums[slow];
            fast=nums[nums[fast]];
        }
        
        int prev;
        slow=0;
        
        while(fast!=slow)
        {
            prev=slow;
            slow=nums[slow];
            fast=nums[fast];
        }
        
        return nums[prev];
    }
};