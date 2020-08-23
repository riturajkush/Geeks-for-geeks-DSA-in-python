#User function Template for python3

def sumSubstrings(s):
    '''
    :param s: given string s, representing a number
    :return: Integer
    '''
    num = list(map(int, s))
    n = len(num)
    if n==1:
        return num[0]
    mod = 10**9+7
    val = n
    inc = "1"
    res = 0
    for i in range(n-1,-1,-1):
        res = res + ((num[i]*val)*(int(inc)))
        #print(((num[i]*val)*(int(inc))))
        inc += "1"
        val -= 1
        #print("res", res)
    return res % mod
    



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
        s = str(input())
        print(sumSubstrings(s))
# } Driver Code Ends
