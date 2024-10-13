#tle for some reason
MOD = 10**9+7

def countWays(n):
    if n == 0:
        return 1
    dp = [0]*(n+1)
    dp[0] = 1
    
    for i in range(1, n+1):
        for j in range(1, 7):
            if j<=i:
                dp[i] = (dp[i] + dp[i-j]) % MOD
    
    return dp[n]

print(countWays(int(input())))