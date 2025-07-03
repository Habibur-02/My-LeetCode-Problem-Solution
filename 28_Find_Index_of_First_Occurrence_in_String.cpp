#include<bits/stdc++.h>
using namespace std;

int main() {
    string haystack = "sadbutsad";
    string needle = "sad";
    int p=needle.size();
    int q=haystack.size();
    // for(int i=0;i<len())
    cout<<p<<" "<<q;
    bool ok=false;

    for (int i=0;i<q;i++)
    {
        if(needle[0]==haystack[i] && i+p-1>=q)
        {
            bool boom=true;
            int l=i+1;
            for(int k=1;k<p;k++)
            {
                if(needle[k]!=haystack[l]) boom=false;
                else l++;
            }
            if (boom==true)
            {
                ok=true;

            }
        }


        if(ok)
        {
            break;
        }
    }


    cout<<ok;

    return 0;
}
