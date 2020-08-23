#User function Template for python3
'''
	Your task is to return the case sorted string
	as described in the problem statement above.
	
	Function Arguments: string s and size n. 
	Return Type: string
'''
def caseSort(s,n):
    lowercase = []
    uppercase = []
    for i in s:
        if ((ord(i)>=65) and (ord(i)<=90)):
            uppercase.append(i)
        if ((ord(i)>=97) and (ord(i)<=122)):
            lowercase.append(i)
    lowercase = sorted(lowercase, reverse=True)
    uppercase = sorted(uppercase, reverse=True)
    #print(lowercase, uppercase)
    res=""
    for i in s:
        if ((ord(i)>=65) and (ord(i)<=90)):
            res += uppercase.pop()
        if (ord(i)>=97) and (ord(i)<=122):
            res += lowercase.pop()
    return res

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

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(caseSort(s,n))
# } Driver Code Ends
