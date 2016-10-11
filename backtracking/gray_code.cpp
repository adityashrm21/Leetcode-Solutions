class Solution {
public:

    
    void solve(vector<int> &res, int n)
    {
        if(n==1)
        {
            res.push_back(0);
            res.push_back(1);
            return;
        }
        
        solve(res, n-1);
        
        int size=res.size()-1;
        for(int i=size;i>=0;i--)
        {
            int a=(res[i] | (1<<n-1));
            res.push_back(a);
        }
        
    }
    
    vector<int> grayCode(int n) 
    {
        vector<int> res;
        
        if(n>0)
        solve(res,n);
        else
        res.push_back(0);
        
        return res;
    }
};