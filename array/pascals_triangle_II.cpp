class Solution {
public:
    vector<int> getRow(int k) {
        
    vector<int> temp;
    vector<vector<int> > ans;
    
    temp.push_back(1);
    ans.push_back(temp);
    temp.push_back(1);
    ans.push_back(temp);
    temp.clear();
    
    if(k<=1)
    return ans[k];
    
    for(int i=2;i<=k;i++)
    {
        temp.push_back(1);
        for(int j=1;j<i;j++)
        {   
            temp.push_back(ans[i-1][j-1]+ans[i-1][j]);
            
        }
        temp.push_back(1);
        ans.push_back(temp);
        temp.clear();
    }
    
    return ans[k];
    }
};