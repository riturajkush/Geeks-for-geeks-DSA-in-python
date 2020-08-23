#{ 
#Driver Code Starts
#Initial Template for Python 3

import math

def getRightMostSetBit(n):
    return math.log2(n&-n)+1


    
 # } Driver Code Ends

#User function Template for python3

##Complete this function
def posOfRightMostDiffBit(m,n):
    m = int(bin(m).replace("0b",""),2)
    n = int(bin(n).replace("0b",""),2)
    res = bin(m^n).replace("0b","")
    flag =0
    for i in range(0,len(res)):
        val = bin(1<<i).replace("0b","")
        print(val, (int(res,2) & int(val,2)))
        if((int(res,2) & int(val,2))!=0):
            flag =1
            return (i+1)
    if(flag==0):
        return -1


#{ 
#Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        mn=[int(x) for x in input().strip().split()]
        m=mn[0]
        n=mn[1]
        
        print(math.floor(posOfRightMostDiffBit(m,n)))
        
        
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends
