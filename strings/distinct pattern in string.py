#User function Template for python3

'''complete function to search distinct pattern in the given string
   p: pattern given in input
   s: string given in the input'''
def search(p,s):
    
    if(p in s):
        return True
    else:
        return False
    '''j = 0
    flag=0
    num = len(p)
    count = num
    if(len(p)==0):
        return False
    for i in range(0,len(s)):
        if (count!=0):
            if(s[i]==p[j]):
                j = j+1
                count = count-1
            else:
                count = num
                j = 0
        if (count==0):
            return True
        else:
            return True
            flag=1
    if(flag==0):
        return False'''


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
