#{ 
#Driver Code Starts
#Initial Template for Python 3



 # } Driver Code Ends

#User function Template for python3

##Complete this function
def findNthFibonacci(number, dp):
    if (dp[number]==0):
        if (number<=1):
            dp[number] = number
        else:
            dp[number] = findNthFibonacci(number-1, dp) + findNthFibonacci(number-2, dp)
    return dp[number]



#{ 
#Driver Code Starts.



def main():
    dp=[0]*100
    dp[0]=0
    dp[1]=1
    dp[2]=1
    testcases=int(input())
    while(testcases>0):
        number=int(input())
        
        print(findNthFibonacci(number, dp))
        testcases-=1

if __name__=="__main__":
    main()

#} Driver Code Ends
