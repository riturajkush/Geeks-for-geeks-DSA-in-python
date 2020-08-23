import sys
def MinJumps(jumps, n):
    dp = [sys.maxsize]*(n)
    dp[0] = 0
    for i in range(1,n):
        for j in range(0,i):
            if(jumps[j]+j>=i):
                dp[i] = min(dp[i], dp[j]+1)
    if (jumps[0]==0 or dp[n-1]==sys.maxsize):
        return -1
    else:
        return dp[n-1]


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(MinJumps(arr, n))
