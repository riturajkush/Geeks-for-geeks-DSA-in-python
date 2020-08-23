#User function Template for python3

##Complete this function
def maxConsecutiveOnes(x):
    count = 0
    while x!=0:
        print(x)
        #print("@@@",bin(x).replace("0b",""))
        x = x & (x<<1)
        #print("###",bin(x).replace("0b",""))
        count+=1

    return count





#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math





def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        print(maxConsecutiveOnes(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
