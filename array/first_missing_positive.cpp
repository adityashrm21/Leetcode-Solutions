class Solution {
public:

    int segregate(vector<int> &nums)
    {
        int n=nums.size();
        
        int i=0, j=0;
        for(int i=0;i<n;i++)
        {
            if(nums[i]<=0)
            {
                int temp=nums[i];
                nums[i]=nums[j];
                nums[j]=temp;
                j++;
            }
        }
        
        return j;
    }
    
    int missing(vector<int> &nums, int index)
    {
        int n=nums.size();
        if(n==0) return 1;
        
        for(int i=index;i<n;i++)
        {
            if(index+abs(nums[i])-1<n && nums[index+abs(nums[i])-1]>0)
            nums[index+abs(nums[i])-1]=-nums[index+abs(nums[i])-1];
        }
        int i;
        for(i=index;i<n;i++)
        {
            if(nums[i]>0)
            return i+1-index;
        }
        
        return n+1-index;
    }
    int firstMissingPositive(vector<int>& nums) {
        
        int n=nums.size();
        if(n==0) return 1;
        
        if(n==1 && nums[0]==0)
        return 1;
        
        int shift=segregate(nums);
        return missing(nums,shift );
    }
};