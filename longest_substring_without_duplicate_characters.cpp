#include <bits/stdc++.h>
using namespace std;
int main()
{

    string a="bbbbb";
    set<char>set;
    int max=0;
    int s=0;
    int e=0;

   while(s<a.size())
   {

    auto it=set.find(a[s]);
    if(it==set.end())
    {
        if (s-e+1>max)
        {
            max=abs(e-s)+1;
        }
        set.insert(a[s]);
        s++;
    }
    else{

        set.erase(a[e]);
        e++;
    }


   }

  cout<<max;



}


// LeetCode Full Solution
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        string a=s;
    set<char>set;
    int max=0;
    int st=0;
    int e=0;

   while(st<a.size())
   {

    auto it=set.find(a[st]);
    if(it==set.end())
    {
        if (st-e+1>max)
        {
            max=abs(e-st)+1;
        }
        set.insert(a[st]);
        st++;
    }
    else{

        set.erase(a[e]);
        e++;
    }


   }

 return max;

    }
};