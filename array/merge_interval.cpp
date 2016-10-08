/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:

    static bool Mycompare(Interval a, Interval b)
    {
        return a.start<b.start;
    }
    
    vector<Interval> insert(vector<Interval>& inter, Interval newI) {
    
        int n=inter.size();
        stack<Interval> s;
        vector<Interval> ans, v;
        
        if(n==0)
        {
            ans.push_back(newI);
            return ans;
        }
        
        inter.push_back(newI);
        
        sort(inter.begin(), inter.end(), Mycompare);
        
        s.push(inter[0]);
        n=inter.size();
        for(int i=1;i<n;i++)
        {
            Interval temp=s.top(), cur=inter[i];
            
            
            if(cur.start>temp.end)
            {
                s.push(cur);
                
            }
            else if(temp.end<cur.end)
            {
                s.pop();
                temp.end=cur.end;
                s.push(temp);
            }
            else continue;
        }
        
        while(!s.empty())
        {
            v.push_back(s.top());
            s.pop();
            
        }
        
        int j=v.size()-1;
        while(j>=0)
        {
            ans.push_back(v[j]);
            j--;
        }
        
        return ans;
        
    }
};