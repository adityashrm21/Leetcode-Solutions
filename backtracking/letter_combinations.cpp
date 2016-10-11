class Solution {
public:
    void letter(vector<string> &ans, string path, vector<string> &inp, string digits, int k)
    {
        if(path.length()==digits.length())
        {
            ans.push_back(path);
            return;
        }
        
        
        /*if( k<inp[digits[ctr]-'0'].length())
        {
            letter(ans, path+inp[digits[ctr]-'0'][k], inp, digits, k+1, ctr+1);
            path.pop_back();
        }*/
        
        
        for(int i=k;i<=digits.length();i++)
        {
            for(int j=0;j<inp[digits[i-1]-'0'].length();j++)
            {
                if( path.length()==i-1)
                {
                    path+=inp[digits[i-1]-'0'][j];
                    letter(ans,path,inp,digits, k+1);
                    path.pop_back();
                }
            }
        }
        
    }
    
    vector<string> letterCombinations(string digits) 
    {
        //int l=digits.length();
        vector<string>inp(10,"");
        inp[2]="abc";
        inp[3]="def";
        inp[4]="ghi";
        inp[5]="jkl";
        inp[6]="mno";
        inp[7]="pqrs";
        inp[8]="tuv";
        inp[9]="wxyz";
        vector<string> ans;
        if(digits=="")
        return ans;
        letter(ans,"", inp, digits, 1);
        
        return ans;
    }
};