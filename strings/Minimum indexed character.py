#User function Template for python3
'''
    Your task is to  find the character in p that
	is present at the minimum index in string s.
	
	Function Arguments: s and p (given strings)
	Return Type: char or string

'''

def minIndexchar(s,p):
    flag = 0
    for i in s:
        if (i in p):
            print(i, end="")
            flag = 1
            break
    if (flag==0):
        print("No character present",end="")
        



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
        p=str(input())
        minIndexchar(s,p)
        print()
# } Driver Code Ends
