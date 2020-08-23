def countOccurence(arr,n,k):
    num = max(arr)
    #print(num)
    res = [0]*(num+1)
    #print(res)
    for i in range(0,n):
        res[arr[i]] += 1
    
    for i in range(0,num):
        if (res[i]>(n//k)):
            return res[i]
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=list(map(int,input().split()))
            
            K=int(input())
            
            print(countOccurence(A, N, K))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
