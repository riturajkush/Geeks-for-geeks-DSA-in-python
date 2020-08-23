#User function Template for python3
'''
Function Arguments :
		@param  : s(given string)
		@return : Modified String or "Empty String"
'''
def removePair(s):
    s = list(s)
    stk = []
    flag = 0
    top = -1
    for i in range(len(s)-1,-1,-1):
        if (top==-1):
            stk.append(s[i])
            top += 1
            continue
        if (s[i]==stk[top]):
            stk.pop()
            top -= 1
        else:
            stk.append(s[i])
            top += 1
            
    stk.reverse()        
    res = "".join(stk)
    if(top!=-1):
        return res
    else:
        return "Empty String"
        
            
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
        print(removePair(str(input())))
# } Driver Code Ends
