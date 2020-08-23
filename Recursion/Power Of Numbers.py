#User function Template for python3

#Complete this function
def power(x,y):
    #mod = 10**9+7
    if(y == 0): return 1
    temp = power(x, int(y / 2))  
      
    if (y % 2 == 0): 
        return ((temp%1000000007) * (temp%1000000007))%1000000007 
    else: 
        if(y > 0): return ((x%1000000007) * (temp%1000000007) * (temp%1000000007))%1000000007
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        
        ans=power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
