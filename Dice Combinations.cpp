#include <bits/stdc++.h>

using namespace std;

const int MOD = 1000000007;

int countWays(int n) {
    if (n == 0) {
        return 1;
    }
    vector<int> dp(n + 1, 0);
    dp[0] = 1;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= 6; ++j) {
            if (j <= i) {
                dp[i] = (dp[i] + dp[i - j]) % MOD;
            }
        }
    }

    return dp[n];
}

int main() {
    int n;
    cin >> n;
    cout << countWays(n) << endl;
    return 0;
}
