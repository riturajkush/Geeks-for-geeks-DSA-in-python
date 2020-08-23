#User function Template for python3

''' Your task is to check if the given string is
	a panagram or not.
	
	Function Arguments: s (given string)
	Return Type: boolean
'''
def checkPanagram(s):
    mark = [0]*26
    for i in s:
        val = ord(i)
        if (val>=65) and (val<=90):
            if (mark[val-65]==1):
                continue
            else:
                mark[val-65] = 1
        elif (val>=97) and (val<=122):
            if (mark[val-97]==1):
                continue
            else:
                mark[val-97] = 1
        else:
            continue
    for i in mark:
        if (i==0):
            return False
    return True


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
        if(checkPanagram(s)):
            print(1)
        else:
            print(0)
# } Driver Code Ends
