#include<bits/stdc++.h>
using namespace std;
int divide(int arr[], int start, int end, int i)
{

    // if(start==end) 
    // {
    //     cout<<"Information I= ";
    //     cout<<arr[start]<<'\n';
    //     return;
    // }
    // int mid=start + end;
    // mid/=2;
    // divide(arr, start, mid,i+1);
    // divide(arr, mid+1, end,i+1);
        if(start==end) 
    {
        cout<<"Information I= ";
        cout<<arr[start]<<'\n';
        return arr[start];
    }
    int mid=start + end;
    mid/=2;
    return max(divide(arr, start, mid,i+1), divide(arr, mid+1, end,i+1));

}
int main()
{

    int arr[10];
    for(int i=0;i<10;i++)
    {
        arr[i]=i+1;
        
    }
    // for(int i=0;i<10;i++) cout<<arr[i]<<" ";
    cout<<divide(arr, 0, 10-1, 0);
    // cout<<divide(arr, 0, 9/2,0);


}