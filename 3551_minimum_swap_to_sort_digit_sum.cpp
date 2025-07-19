#include <bits/stdc++.h>
#define ll long long 
#define nl '\n'
#define yes cout<<"YES"

using namespace std;


class Solution {
public:
    // Helper function to calculate sum of digits
    int f(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }

    // Main function to calculate minimum swaps
    int minSwaps(vector<int>& nums) {
        vector<pair<pair<int, int>, int>> ans;
        for (int i = 0; i < nums.size(); i++) {
            int ele = f(nums[i]);
            ans.push_back({{ele, nums[i]}, i});
        }

        // Sort based on sum of digits first, then the number itself
        sort(ans.begin(), ans.end());

        int n = nums.size();
        int res = 0;
        vector<bool> vis(n, false);

        for (int i = 0; i < n; i++) {
            if (vis[i] || ans[i].second == i) continue;
            int c = 0;
            int j = i;
            while (!vis[j]) {
                vis[j] = true;
                j = ans[j].second;
                c++;
            }
            if (c > 1) res += c - 1;
        }
        return res;
    }
};

int main() {
    Solution obj;
    vector<int> nums = {21, 12, 33, 14};  // Example input
    cout << "Minimum swaps required: " << obj.minSwaps(nums) << endl;
    return 0;
}
