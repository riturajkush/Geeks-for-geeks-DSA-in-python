#User function Template for python3
'''
	Your task is to return the count of number
	of islands in the given boolean grid.
	
	Function Arguments: A (boolean grid), N -> no of rows, M -> no of columns. 
	Return Type: Integer denoting the number of islands
	
	Contributed By: Nagendra Jha
'''
import sys
sys.setrecursionlimit(100000)

def isSafe(A, i, j, visited, N, M):
    return (i>=0 and i<N and j>=0 and j<M and (not visited[i][j]) and A[i][j])
    

def DFS(A, i, j, visited, N, M):
    rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
    colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
    visited[i][j] = True
    for k in  range(8):
        if isSafe(A, i+rowNbr[k], j+colNbr[k], visited, N, M):
            DFS(A, i+rowNbr[k], j+colNbr[k], visited, N, M)


def findIslands(A, N, M):
    visited = [[False for i in range(M)] for j in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if (visited[i][j]==False and A[i][j]==1):
                DFS(A, i, j, visited, N, M)
                count += 1
    return count



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
        n,m = map(int,input().strip().split())
        cell_info = list(map(int,input().strip().split()))
        a = []
        k = 0 # current index
        # create the boolean matrix from cell information
        for i in range(n):
            row_i = []
            for j in range(m):
                row_i.append(cell_info[k])
                k+=1
            a.append(row_i)
        print(findIslands(a,n,m))
# } Driver Code Ends
