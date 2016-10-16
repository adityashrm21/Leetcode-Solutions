class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
     
     int n=A.size();
     vector<int> aux(n+1,0);
     aux[3]=1;
     int diff=2;
     
     vector<int> dp(n,0);
     for(int i=4;i<=n;i++)
     {
         aux[i]=aux[i-1]+diff;
         diff++;
     }
     
     
     
     for(int i=2;i<n;i++)
     {
         if(A[i]-A[i-1]==A[i-1]-A[i-2])
         {
             if(dp[i-1])
             dp[i]=dp[i-1]+1;
         
             else
             dp[i]=3;
         }

     }
     
     int count=0;
     for(int i=2;i<n;i++)
     {
         if(i<n-1)
         {
             if(dp[i]>0 && dp[i+1]==0)
             {
                 count+=aux[dp[i]];
             }
         }
         else count+=aux[dp[i]];
     }
     
     return count;
           
    }
};