#User function Template for python3
'''
	Your task is to sort the elements according
	to the frequency of their occurence
	in the given array.
	
	Function Arguments: array a with size n. 
	Return Type:none, print the sorted array

'''
def values(dic):
    return dic.values

def sortByFreq(arr,n):
    dic = dict()
    for i in arr:
        if(i not in dic):
            dic[i] = 1
        else:
            dic[i] += 1
    val = max(dic)
    #print(dic)
    
    #print(a)
    a = sorted(dic.values(), reverse=True)
    #print(a)
    for j in a:
        for i in sorted(dic.keys()):
            if(j==dic.get(i)):
                for k in range(j):
                    print(i,end=" ")
                dic[i] = 0
                break
    print()
                
        
        
    
        
        



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
        a = list(map(int, input().strip().split()))
        sortByFreq(a,n)
# } Driver Code Ends
