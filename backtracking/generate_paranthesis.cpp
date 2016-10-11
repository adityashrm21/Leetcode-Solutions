class Solution {
public:



    void comb(int n,string path, vector<string> &ans, int k)
    {
        if(k==0 && n==0)
        {
            //sort(path.begin(),path.end());
            ans.push_back(path);
            return;
        }
    
        if(k>0) comb(n,path+")", ans, k-1);
        if(n>0) comb(n-1, path+"(", ans, k+1);
    }
    
    vector<string> generateParenthesis(int n) {
        
        vector<string> ans;

        comb(n,"",ans, 0);

        return ans;   
    }
};
