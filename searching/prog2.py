def searchInSorted(A,N,K):
    l = 0
    r = N-1
    return binarySearch(A, l, r, K)

def binarySearch(A, l, r, K):
    #print(l,r)
    if (l<=r):
        mid = l + (r-l)//2
        if(A[mid]==K):
            #print("A")
            return 1
        if(K<A[mid]):
            #print("B")
            return binarySearch(A, l, mid-1, K)
        if(K>A[mid]):
            #print("C")
            return binarySearch(A, mid+1, r, K)
    #print("D")
    return -1



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NK=(input().strip().split())
            N=int(NK[0])
            K=int(NK[1])
            
            A=[int(x) for x in input().strip().split()]
            
            
            
            print(searchInSorted(A,N,K))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
