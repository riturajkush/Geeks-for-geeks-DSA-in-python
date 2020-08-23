#User function Template for python3

def countWays(n):
    '''
    :param n: given value of n
    :return: Integer , ways to write n as sum of positive integers
    '''
    mod = 1000000007
    if(n==0) or (n==1):
        return 1
    elif(n==2):
        return 2
    else:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%mod
     
        return dp[i]



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
        m = int(input())
        print(countWays(m))
# } Driver Code Ends
