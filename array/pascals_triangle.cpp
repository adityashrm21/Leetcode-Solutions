class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        
        vector<vector<int>> ans;
        if(numRows==0) return ans;
        vector<int> aux;
        aux.push_back(1);
        ans.push_back(aux);
         if(numRows==1) return ans;
        aux.push_back(1);
        ans.push_back(aux);
         if(numRows==2) return ans;    
         //cout<<ans.size();
        for(int i=2;i<numRows;i++)
        {
            vector<int> aux;
            aux.push_back(1);
            for(int j=1;j<ans[i-1].size();j++)
            {
                aux.push_back(ans[i-1][j]+ans[i-1][j-1]);
            }
            aux.push_back(1);
            ans.push_back(aux);
        }
            
        return ans;
    }
};