// C++17
static constexpr int MOD = 1'000'000'007;

class Solution {
public:
    int countPermutations(vector<int>& c) {
        int n = c.size();
        for (int i = 1; i < n; ++i) {
            if (c[i] <= c[0]) return 0;
        }
        long long ans = 1;
        for (int x = 2; x < n; ++x) {
            ans = ans * x % MOD;
        }
        return (int)ans;
    }
};

