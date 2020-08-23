#{ 
#Driver Code Starts
#Initial Template for Python 3


 # } Driver Code Ends

#User function Template for python3

##Complete this function
def findNthFibonacci(number):
    f = [0]*(number+1)
    f[0] = 0
    f[1] = 1
    for i in range(2,number+1):
        f[i] = f[i-1] + f[i-2]
    return f[number]
    
        




#{ 
#Driver Code Starts.

def main():
  
    testcases=int(input())
    while(testcases>0):
        number=int(input())
        
        print(findNthFibonacci(number))
        testcases-=1

if __name__=="__main__":
    main()

#} Driver Code Ends
