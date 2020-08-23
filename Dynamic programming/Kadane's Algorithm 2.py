#{ 
#Driver Code Starts
#Initial Template for Python 3



 # } Driver Code Ends

#User function Template for python3
import sys
def maximumSum(arr,sizeOfArray):
    dp=[0]*sizeOfArray
    dp[0]=max(dp[0],arr[0])
    dp[1]=max(dp[0],arr[1])
    for i in range(2,sizeOfArray):
        dp[i]=max(dp[i-2]+arr[i],dp[i-1])
    if dp[-1] <= 0:
        return max(arr)
    return dp[i]
        
    



#{ 
#Driver Code Starts.


def main():
    testcases=int(input())
    while(testcases>0):
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        print(maximumSum(arr,sizeOfArray))
        testcases=testcases-1

if __name__=="__main__":
    main()

    
#} Driver Code Ends
