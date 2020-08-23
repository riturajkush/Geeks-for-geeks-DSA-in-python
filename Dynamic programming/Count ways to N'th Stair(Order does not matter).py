#User function Template for python3

def countWays(n):
    '''
    :param n: given value of n
    :return: Integer , ways to write n as sum of positive integers
    '''
    ways = [0]*(n+1)
    
    ways[0] = 1
    ways[1] = 1
    
    for i in range(2,n+1):
        ways[i] = (ways[1] + ways[i-2])%1000000007
    
    return ways[n]

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
