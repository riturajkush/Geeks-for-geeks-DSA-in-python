#User function Template for python3


##Complete this function
def swapBits(n):
    i =1
    temp = 0
    while(n>0):
        k = (n//2)%2
        j = n%2
        temp += i*k
        i = 2*i
        temp += i*j
        i = i*2
        n = n//4
    return temp

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        print(swapBits(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
