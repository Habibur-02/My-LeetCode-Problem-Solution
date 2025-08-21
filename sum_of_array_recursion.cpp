#include<bits/stdc++.h>
using namespace std;
int divide(vector<int> & v, int start, int end, int k)
{
    if(start==end)
    {
        return v[start];
        
        

    }
    int mid=start + end;
    mid/=2;
    return (divide(v,start, mid, k) + divide(v, mid+1,end, k));
    // return false;
}
int main()
{

    vector<int>v={10,1,9,2,8,3,7,4,6,5};
    int k=5;
    int n=v.size();
    cout<<divide(v,0,n-1, k);

    // cout<<n;
}