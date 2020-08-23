#User function Template for python3

#Complete this function
def printfrequency(A,N):
    for i in range(0,N):
        A[i] -= 1
        
    for i in range(0,N):
        A[A[i]%N] = A[A[i]%N] + N

    for i in range (0,N):
        print(A[i]//N,end=" ")
    
    




#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        printfrequency(A,N)
        
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
