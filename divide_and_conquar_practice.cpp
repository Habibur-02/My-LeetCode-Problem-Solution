#include <bits/stdc++.h>
using namespace std;
int divideConquar(string s, int start, int end, int k)
{
 if (s.size()<k) return 0;
 int countmap[26]={0};
 for (int i=0;i<26;i++) countmap[s[i]-'a']++;
 for(int i=0;i<26;i++) cout<<countmap[i]<<" ";
 



}
int main()
{

    string s="aaaabbvavavavvbbbbbabbab";
    int k=2;
    int n=s.size();
    int ans=divideConquar(s,0,n,k);

}