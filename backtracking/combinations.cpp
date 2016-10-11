class Solution {
public:
    void comb(int n, int k, vector<vector<int> > &ans, vector<int>& path)
    {
        if(k==0)
        {
            //sort(path.begin(),path.end());
            ans.push_back(path);
            return;
        }
        
        for(int i=n;i>=1;i--)
        {
            path.push_back(i);
            comb(i-1,k-1,ans,path);
            path.pop_back();
        }
    }
    
    
    vector<vector<int>> combine(int n, int k)
    {
        vector<vector<int> > ans;
        vector<int> path;
        comb(n,k,ans,path);

        return ans;
        
    }
};