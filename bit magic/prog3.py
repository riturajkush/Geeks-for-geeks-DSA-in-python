#{ 
#Driver Code Starts
#Initial Template for Python 3

import math


 # } Driver Code Ends

#User function Template for python3
##Complete this code
def checkKthBit(n,k):
    res = int(n & (1<<k))
    if (res==0):
        return 0
    else:
        return 1


#{ 
#Driver Code Starts.


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        k=int(input())
        
        if checkKthBit(n,k):
            print("Yes")
        else:
            print("No")
        
        T-=1

if __name__=="__main__":
    main()
#} Driver Code Ends
