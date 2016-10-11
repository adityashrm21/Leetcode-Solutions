class Solution {
public:
    bool ispal(string s, int i, int j)
    {

        while(i<=j)
        {
            if(s[i]!=s[j]) return false;
            else
            {
                i++; 
                j--;
            }
        }
        return true;
    }

    void getpal(vector<vector<string> > &ans, string s, vector<string> &path, int k)
    {
        //cout<<"this is k: "<<k<<endl;
        
        if(k==s.size())
        {
            ans.push_back(path);
            //path.clear();
            return;
        }

        for(int i=k;i<s.length();i++) 
        {
             
            if(ispal(s,k,i))
            {
                //cout<<"k: "<<k<<endl;
                //cout<<s.substr(k,i)<<endl;
                path.push_back(s.substr(k,i-k+1));
                
                getpal(ans,s,path,i+1);
                path.pop_back();
            }

        }

        
    }
    
    vector<vector<string>> partition(string s) 
    {
        int n=s.length();
        vector<vector<string>> ans;
        vector<string> path;
        
        getpal(ans, s, path,0);
        return ans;
    }
};