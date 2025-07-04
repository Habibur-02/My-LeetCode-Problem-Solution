#include <bits/stdc++.h>
using namespace std;

int main() {

    // Creating an empty vector
    vector<int>v;

    int n;
    cin>>n;

    for (int i=0;i<n;i++)
    {
        int x;
        cin>>x;
        v.push_back(x);
    }
    sort(v.begin(),v.end());
    auto it=find(v.begin(),v.end(),9);
    // cout<<it;
    // for(int i=0;i<v.size();i++)
    // cout<<v[i]<<" ";
    cout<<distance(v.begin(),it);
    
    return 0;
}


