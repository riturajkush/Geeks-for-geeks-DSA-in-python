#User function Template for python3
ans = []
def powerSet(s):
    '''
    :param s: given string s
    :return: list containing power set of s.
    '''
    global ans
    ans = []
    n = len(s)
    res = ""
    i = 0
    finalPowerSet(res, n, s, i)
    return ans
    
def finalPowerSet(res, n, s, i):
    if(i==(n)):
        ans.append(res)
        return
    finalPowerSet(res, n, s, i+1)
    finalPowerSet(res+s[i], n, s, i+1)
    return

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
        s = str(input())
        ans = powerSet(s)
        ans.sort()
        print(*ans)
# } Driver Code Ends
