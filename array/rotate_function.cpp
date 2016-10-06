class Solution {
public:
    int maxRotateFunction(vector<int>& A) {
        
        int n=A.size();
        if(n==0) return 0;
        int ans=INT_MIN, sum=0, curval=0;
        for(int i=0;i<n;i++)
        {
            sum+=A[i];
            curval+=i*A[i];
        }
        
        
        for(int start=0;start<n;start++)
        {
            curval+=A[start]*n-sum;
            ans=max(ans,curval);
        }
        return ans;
    }
};