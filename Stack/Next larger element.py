#User function Template for python3
'''
Function Arguments : 
		@param  : arr(given array), n(size of array)
		@return : Print the Nge of corresponding Elements of array.
'''
def nextLargerElement(arr,n):
    stk = []
    res= []
    stk.append(arr[n-1])
    top = 0
    for i in range(n-2,-1,-1):
        while(top!=-1) and (stk[top]<=arr[i]):
            stk.pop()
            top -= 1
        if (top==-1):
            res.append(-1)
        else:
            res.append(stk[top])
        stk.append(arr[i])
        top += 1
    for i in range(len(res)):
        print(res.pop(),end=" ")
    print("-1",end=" ")
    print()



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

        a = list(map(
