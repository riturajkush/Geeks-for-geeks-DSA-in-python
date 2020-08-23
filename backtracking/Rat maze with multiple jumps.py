def printSolution(sol, N): 
    for i in range(N): 
        for j in range(N): 
            print(sol[i][j], end = " ") 
        print()  

def isSafe(maze, x, y, N): 
    if (x >= 0 and x < N and y >= 0 and 
         y < N and maze[x][y] != 0): 
        return True
    return False
    
def solve(N, maze): 
    sol = [ [ 0 for j in range(N) ] for i in range(N) ] 
    if (solveMazeUtil(maze, 0, 0, sol, N) == False): 
        print("-1") 
        return False
    printSolution(sol, N) 
    return True

def solveMazeUtil(maze, x, y, sol, N): 
    if (x == N - 1 and y == N - 1) : 
        sol[x][y] = 1
        return True
          
    if (isSafe(maze, x, y, N) == True): 
        sol[x][y] = 1
        m = 1
        for i in range(1, N): 
            if (i <= maze[x][y]): 
                if (solveMazeUtil(maze, x,  y+i, sol, N) == True):  
                    return True
                if (solveMazeUtil(maze, x+i,  y, sol, N) == True): 
                    return True
        sol[x][y] = 0
        return False
    return False

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def print_sol(n, sol):
    for i in range(n):
        for j in range(n):
            print(sol[i][j], end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    while(t>0):
        n = int(input())
        maze = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            maze[i] = [int(x) for x in input().strip().split()]
        solve(n, maze)
        t=t-1
# } Driver Code Ends
