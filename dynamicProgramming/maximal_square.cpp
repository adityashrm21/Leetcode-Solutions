class Solution {
public:

    int lrh(vector<int> height)
    {
       
        stack<int> s;
        
        height.push_back(0);
        int n=height.size();
        
        int area=0, cur;
        
        for(int i=0;i<n; )
        {
            if(s.empty() || height[i]>=height[s.top()])
            {
                s.push(i);
                i++;
            }
            else
            {
                int t=height[s.top()];
                s.pop();
                
                if(s.empty())
                {
                    t=min(t,i);
                    
                }
                else t=min(t,i-1-s.top());
                
                cur=t*t;
                //cur=t*(s.empty()?i:i-s.top()-1);
                area=max(area,cur);
            }
        }
        
        return area;
    }
    
    int maximalSquare(vector<vector<char>>& matrix) {
        
        int n=matrix.size();
        int m=n>0?matrix[0].size():0;
        
        int ans=0;
        
        vector<int> heights(m,0);
        
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(matrix[i][j]=='0')
                heights[j]=0;
                else heights[j]+=1;
            }
            
            int cur=lrh(heights);
            ans=max(cur, ans);
        }
        
        return ans;
        
    }
};