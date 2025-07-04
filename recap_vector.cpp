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
    for(int i=0;i<v.size();i++)
    cout<<v[i]<<" ";
    return 0;
}


