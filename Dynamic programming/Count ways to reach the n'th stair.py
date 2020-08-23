#User function Template for python3
def countWays(m):
    '''
    :param n: given value of n
    :return: Integer , ways to write n as sum of positive integers
    '''
    if m == 0 or m == 1:
        return 1
    if m == 2:
        return 2
    a = 1
    b = 1
    for i in range(2, m+1):
        d = (a+b)%(1000000007)
        a = b
        b = d
    return d  



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
