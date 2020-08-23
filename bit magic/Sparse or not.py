#User function Template for python3

##Complete this function
def isSparse(n):
    n = bin(n).replace("0b","")
    #print(n)
    for i in range(len(n)-1):
        if(int(n[i],2) & int(n[i+1],2)==1):
            return False 
        else:
            continue
    return True
        




#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        if isSparse(n):
            print("1")
        else:
            print("0")
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
