#User function Template for python3

#Complete this function
def reverseInGroups(A,N,K):
    i = 0
    j = K-1
    flag=0
    while(flag==0):
        if (j<(N-1)):
            reverseSub(A, i, j)
            i = i+K
            j = j+K
        else:
            j = N-1
            reverseSub(A, i, j)
            flag=1
    return A
    

def reverseSub(A,top,down):
    #print(A)
    if (top>=down):
        return 

    temp = A[top]
    A[top] = A[down]
    A[down] = temp
    
    reverseSub(A, top+1, down-1)

            



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math




def main():
    
    T=int(input())
    
    while(T>0):
        
        nk=[int(x) for x in input().strip().split()]
        
        N=nk[0]
        K=nk[1]
        
        A=[int(x) for x in input().strip().split()]
        
        A=reverseInGroups(A,N,K)
        #print(A)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
