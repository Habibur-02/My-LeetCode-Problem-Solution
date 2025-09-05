#include<bits/stdc++.h>
using namespace std;
int main()
{

    int k=3;
    int n=6;
    vector<int>v(n);
    // v={1,2,3,4,5};
    for(int i=1;i<=n;i++) v[i]=i;
    int ans=0;
    while(k<=n)
    {
    for(int i=1;i+k-1<=n;i++)
    {
        set<int>s;
        for(int j=i;j<=k;j++)
        {
            s.insert(abs(v[j]-v[j+1]));
        }
        if(s.size()==1) 
        {
            ans++;
            cout<<"K="<<k<<" ans="<<ans<<" i="<<i<<'\n';
        }
    }
    k++;
    }

//   cout<<ans;


}