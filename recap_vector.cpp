#include <bits/stdc++.h>
#define ll long long 
using namespace std;

int main() {

    vector<int>v;

    // int n;
    // cin>>n;

    // for (int i=0;i<2;i++)
    // {
    //     int x;
    //     cin>>x;
    //     v.push_back(x);
    // }
    // sort(v.begin(),v.end());
    // auto it=find(v.begin(),v.end(),9);
    // cout<<it;
    // for(int i=0;i<v.size();i++)
    // cout<<v[i]<<" ";
    // if(it==v.end()) cout<<"Not Found"<<'\n';
    // else cout<<distance(v.begin(),it)<<'\n'; //it will print first occurance
    // cout<<distance(v.begin(),it)<<'\n';

    vector<pair<int,int>>v1;
    for(int i=0;i<5;i++)
    {
        int a,b;
        cin>>a>>b;
        v1.push_back({a,b});
    }
    for (auto k:v1) cout<<k.first<<" "<<k.second<<" ";
    cout<<'\n';
    sort(v1.begin(),v1.end());

    for(auto l:v1) cout<<l.first<<" "<<l.second<<" ";

    // for (int i=0;i<5;i++)
    // {


    // }

    return 0;

}


