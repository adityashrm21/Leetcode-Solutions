class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if(matrix.empty()) return 0;
        int m=matrix.size(), n=matrix[0].size(), maxrec=0;
        
        vector<int> height(n,0);
        
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(matrix[i][j]=='0')
                height[j]=0;
                else height[j]++;
            }
            maxrec=max(maxrec, lrh(height));
        }
        
        return maxrec;
    }
    
    int lrh(vector<int> &height)
    {
        stack<int> s;
        height.push_back(0);
        
        int i=0, maxarea=0;
        while( i<height.size())
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
                
                
                int area=t*(s.empty() ? i : i-1-s.top());
                maxarea=max(maxarea, area);
            }
        }
        
        return maxarea;
    }
};