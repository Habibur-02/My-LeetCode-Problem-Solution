#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int DivideAndConquer(string s, int start, int end, int k) {
        if (end - start < k) return 0;
        
        int countmap[26] = {0};
        for (int i = start; i < end; i++) {
            countmap[s[i] - 'a']++;
        }
        
        bool valid = true;
        for (int i = 0; i < 26; i++) {
            if (countmap[i] > 0 && countmap[i] < k) {
                valid = false;
                break;
            }
        }
        if (valid) return end - start;
        
        for (int mid = start; mid < end; mid++) {
            if (countmap[s[mid] - 'a'] < k) {
                int left = DivideAndConquer(s, start, mid, k);
                
                // Skip all consecutive invalid characters
                int midnext = mid + 1;
                while (midnext < end && countmap[s[midnext] - 'a'] < k) {
                    midnext++;
                }
                
                int right = DivideAndConquer(s, midnext, end, k);
                return max(left, right);
            }
        }
        
        return end - start;
    }
    
    int longestSubstring(string s, int k) {
        int n = s.size();
        return DivideAndConquer(s, 0, n, k);
    }
};
// int main()
// {
//  string s="aaabb";
//  int k=3;
//  int n=s.size();
//  vector<int>p(26);
//  int ans=0;
//  for(int i=0;i<26;i++) p[i]=0;

//  for(int i=0;i<n;i++)
//  {
//     for (int j=i+1;j<n;j++)
//     {
//         vector<int>v(26,0);
//         // v=p;
//         string ss=s.substr(i,j+1);
//         cout<<ss<<" --Kaj hocche"<<'\n';

//         for(int l=0;l<ss.size();l++)
//         {
//             v[ss[l]-'a']++;
//         }
//         bool hobe=true;
//         for(int m=0;m<ss.size();m++)
//         {
//             if(v[ss[m]-'a']<k) hobe=false;
            
//         }
//         if(hobe) ans=max(ans,j-i+1);

//     }
//  }

// string ss=s.substr(0,3);
// // cout<<ss;
// cout<<ans;
// string s="aaabb";
// int k=2;
// int n=s.size();
// int ans=DivideAndConquar(s,0,n,k);
// cout<<ans;


// }