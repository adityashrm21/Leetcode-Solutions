class Solution {
public:
    int maxProfit(vector<int>& prices) 
    {
       
        int n=prices.size();
        //vector<int> dp(n,0);
        if(n<2) return 0;

        int states[2][4]={INT_MIN, 0, INT_MIN, 0};
        int cur=0, next=1;
        
        for(int i=0;i<n;i++)
        {
            states[next][0]=max(states[cur][0], -prices[i]);
            states[next][1]=max(states[cur][1], states[cur][0]+prices[i]);
            states[next][2]=max(states[cur][2], states[cur][1]-prices[i]);
            states[next][3]=max(states[cur][3], states[cur][2]+prices[i]);
            swap(cur, next);
        }
        
        return max(states[cur][1], states[cur][3]);
    }
};