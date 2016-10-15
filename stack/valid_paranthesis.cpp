class Solution {
public:
    int isValid(string A) {

    stack<char> s;
    int l=A.length();
    if(l<=1) return 0;
    for(int i=0;i<l;i++)
    {
        if(A[i]=='(' || A[i]=='{' || A[i]=='[')
        s.push(A[i]);
        else
        {
            if(!s.empty())
            {
                char t=s.top();
                if((t=='[' && A[i]!=']') || (t=='(' && A[i]!=')') || (t=='{' && A[i]!='}')) return 0;
                else s.pop();
            }
            else return 0;
        }
    }
    if(!s.empty()) return 0;
    else return 1;
    
    
}

};