#User function Template for python3

# Function to get minimum number of trials needed in worst
# case with n eggs and k floors
INT_MAX = 32767
def eggDrop(n, k):
    dp = [[0 for i in range(k+1)] for j in range(n+1)]
    for i in range(1,n+1):
        dp[i][1] = 1
        dp[i][0] = 0
    for j in range(1,k+1):
        dp[1][j] = j
        
    for i in range(2,n+1):
        for j in range(2,k+1):
            dp[i][j] = INT_MAX
            for x in range(1,j+1):
                res = 1 + max(dp[i-1][x-1], dp[i][j-x])
                if (res<dp[i][j]):
                    dp[i][j] = res
    return dp[n][k]



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k = map(int,input().strip().split())
        print(eggDrop(n,k))
# } Driver Code Ends
