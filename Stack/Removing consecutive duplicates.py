#User function Template for python3
'''
Function Arguments :
		@param  : s(given string)
		@return : Modified String
'''
def removeConsecutiveDuplicates(s):
    stk = []
    s = list(s)
    stk.append(s[0])
    top = 0
    for i in range(1,len(s)):
        if (s[i]!=stk[top]):
            stk.append(s[i])
            top += 1
    #stk.reverse()
    stk = "".join(stk)
    return stk


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        print(removeConsecutiveDuplicates(str(input())))
# } Driver Code Ends
