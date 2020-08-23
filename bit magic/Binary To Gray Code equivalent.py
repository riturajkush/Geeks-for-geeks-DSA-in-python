#User function Template for python3

##Complete this fcuntion
def greyConverter(n):
    n = (bin(n).replace("0b",""))
    res = ""+n[0]
    for i in range(1,len(n)):
        res = res + str(int(n[i])^int(n[i-1]))
    return int(res,2)
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math




def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        print(greyConverter(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
