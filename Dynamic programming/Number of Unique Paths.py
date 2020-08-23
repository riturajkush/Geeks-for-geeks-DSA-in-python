def unique(m, n):
    if(n==1 or m==1):
        return 1
    dp = [[1]*n]*m
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]


t = int(input())
for i in range(t):
    m, n = [int(x) for x in input().split()]
    print(unique(m, n))
