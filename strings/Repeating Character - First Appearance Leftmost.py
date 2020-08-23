#User function Template for python3


'''
	Your task is to return the lefmost index of the repeating 
	character whose first appereance is left most or return
	-1 if all characters are distinct.
	
	Function Arguments: s (given string)
	Return Type: integer
'''

def repeatingCharacter(s):
    val = s[0]
    num = len(s)
    for i in range(2,num):
        if(s[i]==val):
            return i
    return -1



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
        index=repeatingCharacter(s)
        if(index==-1):
            print(-1)
        else:
            print(s[index])
            
# } Driver Code Ends
