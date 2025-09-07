#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{

    string s="AAAAAAAAAAAA";
    

    map<string,int>m;

    for (int i=0;i+10-1<s.size();i++)
    {
        // cout<<s.substr(i,10)<<'\n';
        string p=s.substr(i,10);
        m[p]++;
    }

//   for (auto k:m)
//   cout<<k.first<<" "<<k.second<<'\n';

//  string l="bbbbbbbbbbbbbbbbbbbbbbb";
//  cout<<l.size();

    vector<string>v;
    for(auto K:m)
    {
        if(K.second>1)
        {
            v.push_back(K.first);
        }

    }
    for(int i=0;i<v.size();i++)
    {
        cout<<v[i]<<'\n';

    }

    // cout<<findRepeatedDnaSequences(s);



}

// LeetCode Full Solutiion 

class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
         map<string,int>m;

    for (int i=0;i+10-1<s.size();i++)
    {
        // cout<<s.substr(i,10)<<'\n';
        string p=s.substr(i,10);
        m[p]++;
    }

//   for (auto k:m)
//   cout<<k.first<<" "<<k.second<<'\n';

//  string l="bbbbbbbbbbbbbbbbbbbbbbb";
//  cout<<l.size();

    vector<string>v;
    for(auto K:m)
    {
        if(K.second>1)
        {
            v.push_back(K.first);
        }

    }
    return v;


    }
};