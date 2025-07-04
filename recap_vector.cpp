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
    // sort(v.begin(),v.end());
    auto it=find(v.begin(),v.end(),9);
    // cout<<it;
    // for(int i=0;i<v.size();i++)
    // cout<<v[i]<<" ";
    if(it==v.end()) cout<<"Not Found"<<'\n';
    else cout<<distance(v.begin(),it)<<'\n'; //it will print first occurance
    cout<<distance(v.begin(),it);


    


    
    return 0;

}


