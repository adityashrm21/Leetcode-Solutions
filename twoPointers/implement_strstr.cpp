class Solution {
public:
    int strStr(string haystack, string needle) {
     
     int m=haystack.length(), n=needle.length();
     
     if(m<n) return -1;
     if(n==0) return 0;
     
     for(int i=0;i<m-n+1;i++)
     {
         if(needle[0]==haystack[i])
         {
             if(needle==haystack.substr(i,n))
             return i;
         }
     }
     return -1;
     
    }
};