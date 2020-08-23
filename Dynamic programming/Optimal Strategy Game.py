#User function Template for python3

def optimalStrategyOfGame(arr, n):
    table = [[0 for i in range(n)] for j in range(n)]
    
    for gap in range(n):
        for j in range(gap,n):
            i = j - gap
            x = 0
            if ((i+2)<=j):
                x = table[i+2][j]
            y = 0
            if((i+1)<=(j-1)):
                y = table[i+1][j-1]
            z = 0
            if (i<=(j-2)):
                z = table[i][j-2]
            table[i][j] = max(arr[i]+min(x,y), arr[j]+min(y,z))
    return table[0][n-1]
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        print(optimalStrategyOfGame(arr,n))

# } Driver Code Ends
