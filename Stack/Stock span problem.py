#User function Template for python3
'''
Function Arguments :
		@param  : price( array containing price on days) , n size of list input.
		@return : List containg corresponding span values
'''
def calculateSpan(a,n):
    ''''stk = []
    stk.append(0)
    top = 0
    res = [1]
    for i in range(1,n):
        while (top!=-1) and (a[i]<=a[stk[top]]):
            stk.pop()
            top -= 1
        if (top==-1):
            span = i+1
        else:
            span = i - stk[top]
        res.append(span)
        stk.append(i)
        top += 1
    return res'''
    
    index = []
    index.append(0)

    result = [1]
    top = 0
    for i in range(1, n):
        while( (top != -1) and (a[i] >= a[index[top]])):
            index.pop()
            top -= 1
        if top == -1:
            result.append(i+1)
        else:
            result.append(i - index[top])
        index.append(i)
        top += 1
    return result
            



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nikhil Kumar Singh

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
        print(*calculateSpan(a, n)) # print space seperated elements of span array
# } Driver Code Ends
