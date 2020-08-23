#User function Template for python3
''' 
    Your task is to print boundary traversal
	of a given matrix.
	
	Function Arguments : a(given array), n (no of rows), m (no of columns). 
	Return Type: none, you have to print the result.
'''

def BoundaryTraversal(a,n,m):
    i=0
    for j in range(0,m):
        print(a[i][j],end=" ")
    j=m-1
    for i in range(1,n):
        print(a[i][j],end=" ")
    i=n-1
    if(i>0):
        for j in range(m-2,-1,-1):
            print(a[i][j],end=" ")
        j=0
    if(j<m-1):
        for="" i="" in="" range(n-2,0,-1):="" print(a[i][j],end=" " )="" print()="" <="" code="">
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
#Contributed by : Nagendra Jha

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
    t=int(input())
    for cases in range(t):
        n,m = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        a=[]
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(values[k])
                k+=1
            a.append(row)
        BoundaryTraversal(a,n,m)
        print ()

# } Driver Code Ends
