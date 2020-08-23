#User function Template for python3


##Complete this function
def grayToBinary(n):
    num = n
    while (n>=1):
        n=n>>1;
        num = (num^n)
    return num



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        print(grayToBinary(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
