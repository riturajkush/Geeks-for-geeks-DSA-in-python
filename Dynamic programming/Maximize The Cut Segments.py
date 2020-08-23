#User function Template for python3


def maximizeTheCuts(n,x,y,z):
    dp = [-1]*(n+1)
    dp[0] = 0
    for j in range(1, n+1):
        if(j>=x):
            dp[j] = max(dp[j], dp[j-x])
        if(j>=y):
            dp[j] = max(dp[j], dp[j-y])
        if(j>=z):
            dp[j] = max(dp[j], dp[j-z])
        if(dp[j]!=-1):
            dp[j] += 1
    return max(dp[n],0)



#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        x,y,z=[int(x) for x in input().split()]
        
        print(maximizeTheCuts(n,x,y,z))
# } Driver Code Ends
