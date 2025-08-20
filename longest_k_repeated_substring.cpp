#include <bits/stdc++.h>
using namespace std;
int DivideAndConquar(string s, int start, int end, int k)
{
    
}
int main()
{
 string s="aaabb";
 int k=3;
 int n=s.size();
 vector<int>p(26);
 int ans=0;
 for(int i=0;i<26;i++) p[i]=0;

 for(int i=0;i<n;i++)
 {
    for (int j=i+1;j<n;j++)
    {
        vector<int>v(26,0);
        // v=p;
        string ss=s.substr(i,j+1);
        cout<<ss<<" --Kaj hocche"<<'\n';

        for(int l=0;l<ss.size();l++)
        {
            v[ss[l]-'a']++;
        }
        bool hobe=true;
        for(int m=0;m<ss.size();m++)
        {
            if(v[ss[m]-'a']<k) hobe=false;
            
        }
        if(hobe) ans=max(ans,j-i+1);

    }
 }

string ss=s.substr(0,3);
// cout<<ss;
cout<<ans;
}