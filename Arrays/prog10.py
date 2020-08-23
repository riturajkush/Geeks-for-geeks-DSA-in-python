#User function Template for python3

#Complete this function
def maxOccured(L,R,N,maxx):
    #print(maxx)
    arr = [0]*(maxx+10)
    mnum = max(L)
    #print(mnum)
    
    for i in range(0, N):
        #print(i)
        arr[L[i]] += 1
        arr[R[i]+1] += -1
    #print(arr)
    
    val = arr[0]
    index = 0
    for i in range(1, maxx+10):
        arr[i] += arr[i-1]
        if (val<arr[i]):
            val = arr[i]
            index = i
    #print(arr)
    return index


#{ 
#  Driver Code Starts
#Initial Template for Python 3


import math

A=[0]*1000000


            

def main():
    
    T=int(input())
    
    while(T>0):
        
        global A
        A=[0]*1000000
        
        N=int(input())
        
        L=[int(x) for x in input().strip().split()]
        R=[int(x) for x in input().strip().split()]
        
        maxx=max(R)
        
        print(maxOccured(L,R,N,maxx))
            
        
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
