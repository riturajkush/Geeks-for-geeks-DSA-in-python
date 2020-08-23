#User function Template for python3


def maximumSum(arr,sizeOfArray):
    dp=[0]*sizeOfArray##declaring dp array 
    dp[0]=arr[0]
    answer=arr[0]
    end = arr[0]
    for i in range(1,sizeOfArray):
        ##The maximum sum at dp[i] will be max of (current array element+dp[i-1]) and (current array element)
        end = max(arr[i], end+arr[i])
        dp[i] = end
        #print(dp[i])
        answer=max(answer,dp[i])
    ##dp array print    
    for i in range(sizeOfArray):
        print(dp[i],end=" ")
    print()
    ##print end
    return answer




#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        print(maximumSum(a,n))
# } Driver Code Ends
