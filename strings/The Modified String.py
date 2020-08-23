#User function Template for python3

'''
	Your task is to return minimum no of character
	to be inserted so that no three consecutive
	characters in the string are not same.
	
	Function Arguments: s (given string)
	Return Type: integer
'''
def modified(s):
    count = 1
    res = 0
    for i in range(1,len(s)):
        if (s[i]==s[i-1]):
            #print(s[i])
            count += 1
        else:
            count = 1
        if (count==3):
            #print(s[i], count)
            res += count
            count = 1
            #print(res)
    if (res%3==0):
        return res//3
    else:
        return (res-1)//2
        



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        print(modified(s))
# } Driver Code Ends
