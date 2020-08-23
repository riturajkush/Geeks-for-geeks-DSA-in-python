#User function Template for python3

#Complete this function

def checkbit(pattern, arr, n):
    count = 0
    for i in range(0,n):
        if(pattern & arr[i]==pattern):
            count+= 1
    return count


def maxAND(arr,n):
    res = 0
    for bit in range(31,-1,-1):
        count = checkbit(res | (1<<bit), arr, n)
        if(count>=2):
            res = res | (1<<bit)
    return res



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        
        print(maxAND(arr,n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
