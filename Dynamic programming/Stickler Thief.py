#User function Template for python3

def FindMaxSum(a, n):
    '''
    :param a:  given list of values
    :param n: size of a
    :return: Integer
    '''
    if(n==2 or n==1):
        return max(a)
    dp = [0]*n
    dp[0] = a[0]
    dp[1] = a[1]
    res = dp[0]
    for i in range(2,n):
        dp[i] = a[i] + res
        res = max(res,dp[i-1])
    #print(dp)
    return max(dp[n-1],res)


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
        n = int(input())
        a = list(map(int,input().strip().split()))
        print(FindMaxSum(a,n))
# } Driver Code Ends
