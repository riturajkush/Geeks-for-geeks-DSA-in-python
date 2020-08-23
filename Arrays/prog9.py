#User function Template for python3

##Complete this functiom
def rotateArr(A,D,N):
    reverseSub(A, 0, D-1)
    #print(A)
    reverseSub(A, D, N-1)
    #print(A)
    reverseSub(A, 0, N-1)
    #print(A)
    return A
        
def reverseSub(A,top,down):
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
        
        nd=[int(x) for x in input().strip().split()]
        
        N=nd[0]
        D=nd[1]
        
        A=[int(x) for x in input().strip().split()]
        
        rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
