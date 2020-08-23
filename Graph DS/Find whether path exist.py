#User function Template for python3

def isSafe(M, N, visited, i, j):
    #print("$",i,j)
    #print("^^",M[i][j])
    return (i>=0 and i<N and j>=0 and j<N and (not visited[i][j]) and M[i][j])

def DFS(M, N, visited, i, j):
    #print("*",M[i][j])
    if(M[i][j]==2):
        #print("!!!")
        return 1
    rowNbr = [-1, 1, 0, 0]
    colNbr = [0, 0, -1, 1]
    visited[i][j] = True
    #print("#",i,j)
    #print("@",M[i][j])
    for k in range(4):
        #print("k",k)
        if(isSafe(M, N, visited, i+rowNbr[k], j+colNbr[k])):
            if (DFS(M, N, visited, i+rowNbr[k], j+colNbr[k]))==1:
                return 1
    return 0
    

def is_possible(M, N):
    visited = [[False for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if(M[i][j]==1):
                return DFS(M, N, visited, i, j)
    




#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
import sys
sys.setrecursionlimit(10**6)
from collections import deque
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        mat_val=deque([int(x) for x in input().split()])
        
        mat=[]
        for i in range(N):
            mat.append([])
            for j in range(N):
                mat[i].append(mat_val.popleft())
        
        print(is_possible(mat,N))
        
        
                
                
# } Driver Code Ends
