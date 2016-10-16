class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int n=prices.size();
        vector<int> buy(n,0), sell(n,0);
        if(n<2) return 0;
        buy[0]=-prices[0];

        for(int i=1;i<n;i++)
        {
            if(i==1)
            {
                buy[i]=buy[0]+prices[0]-prices[1];
            }
            else
            {
                buy[i]=max(sell[i-2]-prices[i], buy[i-1]+prices[i-1]-prices[i]);
            }
            sell[i]=max(prices[i]+buy[i-1], sell[i-1]-prices[i-1]+prices[i]);
        }
        
        return *max_element(sell.begin(), sell.end());
    }
};