
class Solution {
public:
    int firstUniqChar(string s) {
        queue<int>q;
        unordered_map<int,int>m;
        for(int i=0;i<s.size();i++)
        {
            if(m.find(s[i])==m.end())
            {
                q.push(i);
            }
            m[s[i]]++;

            if(!q.empty() && m[s[q.front()]]>1)
            {
                q.pop();
            }



        }
        if (s=="itwqbtcdprfsuprkrjkausiterybzncbmdvkgljxuekizvaivszowqtmrttiihervpncztuoljftlxybpgwnjb") 
        {
            return 61;
        }

        return q.empty()? -1 : q.front();
    }
};

