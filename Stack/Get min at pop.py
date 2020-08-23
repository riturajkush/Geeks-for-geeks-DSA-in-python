#User function Template for python3

def _push(a,n):
    '''
    :param a: given array
    :param n: given size of array
    :return: stack
    '''
    val = 100000001
    stk = []
    for i in a:
        val = min(val,i)
        stk.append(val)
    return stk
        
def _getMinAtPop(stack):
    '''
    :param stack: our stack
    :return: none, print the elements in order of pop one by one, new line is not required
    '''
    #print(stack)
    for i in range(0,len(stack)):
        print(stack.pop(),end=" ")
    



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
        n = int(input())
        a = list(map(int,input().strip().split()))
        stack =  _push(a,n) # our stack to be used
        _getMinAtPop(stack) # print elements of stack as required
        print()
# } Driver Code Ends
