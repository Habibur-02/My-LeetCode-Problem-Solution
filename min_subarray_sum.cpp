#include<bits/stdc++.h>
using namespace std;
#define ll long long 
int main()
{

    vector<int>v={1,4,4};
    int target=4;
    int ss=0;

    for (auto l:v) ss+=l;
    if(ss<target) cout<<0;
    if(ss==target) cout<<v.size();

    int s=0;
    int e=0;
    int minm=INT_MAX;
    int sum=0;
    while (s<v.size())
    {
        /* code */
        sum+=v[s];

        if(sum>=target)
        {
            while(e<=s && sum>=target)
            {
            minm=min(minm,s-e+1);
            cout<<"loop no- "<<s<<" "<<e<<" ";
            cout<<minm<<'\n';
            sum-=v[e];
            e++;
            }
            
        }
        s++;


    }
    
   cout<<minm;

}
