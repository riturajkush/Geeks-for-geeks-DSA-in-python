#{ 
#Driver Code Starts
#Initial Template for Python 3




 # } Driver Code Ends

#User function Template for python3


##Complete this function
def minimumNumberOfCoins(coins,numberofcoins, value):
    dp = [float('inf') for i in range(value+1)]
    dp[0] = 0
    for i in coins:
        for j in range(i, value+1):
            dp[j] = min(dp[j], dp[j-i]+1)
   
    return dp[value] if dp[value] != float('inf') else "Not Possible"

        


#{ 
#Driver Code Starts.

def main():
    testcases=int(input())
    while(testcases>0):
        value=int(input())
        numberOfCoins=int(input())
        coins=[int(x) for x in input().strip().split()]
        answer=minimumNumberOfCoins(coins,numberOfCoins,value)
        print("Not Possible") if answer == -1 else print(answer)
        testcases-=1

if __name__=="__main__":
    main()
    
#} Driver Code Ends
