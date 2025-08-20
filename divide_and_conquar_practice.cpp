#include <bits/stdc++.h>
using namespace std;
void divideConquar(string s,int k)
{
if (s.size() <= 1) {
        if (!s.empty()) {
            cout << "String Information: " << s << '\n';
        }
        return;
    }

    cout << "String Information: " << s << '\n';
int mid=s.size()/2;




// cout<<"String Information"<<" "<<s<<'\n';
string a=s.substr(0, mid);
string b=s.substr(mid);

divideConquar(a, k);
divideConquar(b, k);





}
int main()
{

    string s="aabbb";
    int k=1;
    int n=s.size();
    divideConquar(s, k);
    // cout<<s.substr(20,24);

}