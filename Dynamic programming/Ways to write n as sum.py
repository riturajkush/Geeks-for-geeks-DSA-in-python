#User function Template for python3
def countWays(n):
    '''
    :param n: given value of n
    :return: Integer , ways to write n as sum of positive integers
    '''
    mod = 1000000007
    table =[0] * (n + 1) 
  
    # Base case (If given value is 0) 
    # Only 1 way to get 0 (select no integer) 
    table[0] = 1
  
    # Pick all integer one by one and update the 
    # table[] values after the index greater 
    # than or equal to n 
    for i in range(1, n ): 
  
        for j in range(i , n + 1): 
  
            table[j] = (table[j] +  table[j - i])%mod            
  
    return table[n] 
    



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
        print(countWays(n))

# } Driver Code Ends
