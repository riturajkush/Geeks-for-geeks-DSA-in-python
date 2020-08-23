#User function Template for python3


##Complete this function
def isPowerofTwo(n):
    n = bin(n).replace("0b","")
    if(n.count("1")==1):
        return True
    else:
        return False



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        if isPowerofTwo(n):
            print("YES")
        else:
            print("NO")
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
