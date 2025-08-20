#include <bits/stdc++.h>
using namespace std;
int divideConquar(string s, int start, int end, int k)
{
 if (s.empty()) return 0;
 int countmap[26]={0};
//  for (int i=0;i<26;i++) countmap[s[i]-'a']++;
//  for(int i=0;i<26;i++) cout<<countmap[i]<<" ";
int mid=start+end;
mid=mid/2;



cout<<"String Information"<<" "<<s<<" start "<<start<<" end "<<end<<'\n';
string a=s.substr(start, mid);
string b=s.substr(mid, end);

return divideConquar(a, start, mid, k) + divideConquar(b, mid,end, k);





}
int main()
{

    string s="aaaabbvavavavvbbbbbabbab";
    int k=1;
    int n=s.size();
    // int ans=divideConquar(s,0,n,k);
    cout<<s.substr(20,24);

}