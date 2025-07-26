#include<bits/stdc++.h>
using namespace std;
int main()
{
   vector<int>v = {99,99};
   int  k = 1;


//    map<int, vector<int>>m;
// //    m[1].push_back(3);
// int lll=0;
//   for(auto u:v) m[u].push_back(lll++);
   
// for(auto &l:m)
// {
//    sort(l.second.begin(),l.second.end());
// }
 
//    for(auto &l:m)
//    { cout<<l.first<<"--->";
//     for(auto &p:l.second)
//         cout<<" "<<p;
//     cout<<'\n';
//    }
//    int n=4;
//   bool ok=false;
//    for (auto &p:m)
//    {
//     int diff;
//     int ll=p.second.size();
//     if(ll==1) {diff=1;}
//     else diff=-p.second[0]+p.second[ll-1]+1;
//     if(diff<=k){ok=true; 
//     }
//     if(ok) break;

//    }
//   cout<<ok;
    
map<int, vector<int>>m;
 if(k>=v.size()) cout<<false;
//    m[1].push_back(3);
int lll=0;
  for(auto &u:v) m[u].push_back(lll++);
   
for(auto &l:m)
{
   sort(l.second.begin(),l.second.end());
}
 
//    for(auto &l:m)
//    { cout<<l.first<<"--->";
//     for(auto &p:l.second)
//         cout<<" "<<p;
//     cout<<'\n';
//    }
   int n=v.size();
  bool ok=false;
   for (auto &p:m)
   {
    int diff;
    int ll=p.second.size();
    if(ll==1) {diff=1;}
    else diff=-p.second[0]+p.second[ll-1];
    if(diff<=k){ok=true; 
    }
    if(ok) break;

   }
   cout<<ok;





}