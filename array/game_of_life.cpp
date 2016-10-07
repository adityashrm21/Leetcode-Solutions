class Solution {
public:

    bool isSafe(int m, int n, int row, int col)
    {
        if(row<0 || row>m-1 || col<0 || col>n-1)
        return false;
        
        return true;
    }
    void gameOfLife(vector<vector<int>>& board) {
        
        int xMove[8] = {  -1, 0, 1, 1, 1, 0, -1, -1};
        int yMove[8] = {  -1,-1, -1, 0, 1, 1, 1, 0 };
        int m=board.size();
        int n=board[0].size();
        
        vector<vector<int> > aux(m, vector<int>(n));
        
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                int status=board[i][j], nearL=0, nearD=0;
                
                for(int k=0;k<8;k++)
                {
                    if(isSafe(m,n,i+xMove[k],j+yMove[k]))
                    {
                        if(board[i+xMove[k]][j+yMove[k]]==0)
                        nearD++;
                        else nearL++;
                    }
                }
                
                //cout<<"nearL: "<<nearL<<" nearD: "<<nearD<<endl;
                
                if(status==1 && nearL<2) aux[i][j]=0;
                else if(status==1 && nearL>3) aux[i][j]=0;
                else if(status==0 && nearL==3) aux[i][j]=1;
                else aux[i][j]=board[i][j];
            }
        }
        
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                board[i][j]=aux[i][j];
            }
        }

        return;
    }
};