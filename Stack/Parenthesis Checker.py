#User function Template for python3
'''
Function Arguments :
		@param  : s (given string containing parenthesis) 
		@return : boolean True or False
'''
def ispar(m):
    m = list(m)
    stk = []
    top = -1
    for i in range(0,len(m)):
        if ((m[i]=='(') or (m[i]=='{') or (m[i]=='[')):
            stk.append(m[i])
            top += 1
        else:
            if(top>=0):
                val = stk.pop()
                top -= 1
                if ((val=='(' and m[i]==')') or (val=='{' and m[i]=='}') or (val=='[' and m[i]==']')):
                    continue
                else:
                    return 0
            else:
                return 0
        #print("111", stk, top)
    #print("final stack", stk)
    if (len(stk)==0):
        return 1
    else:
        return 0



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
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        if ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends
