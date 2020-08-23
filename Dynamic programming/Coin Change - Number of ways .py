#{ 
#Driver Code Starts
#Initial Template for Python 3




 # } Driver Code Ends

#User function Template for python3

##Complete this function
def numberOfWays(coins,numberOfCoins,value):
    ways=[0]*(value+1)
    '''
    We declare an array that will contain the number of--
    ways to make change for all values from 0 to value
    This is done as we are working from bottom up. So, obviously, we need to make change for smaller values--
    before we can make change for the given values.
       
    '''
    ways[0]=1#We can make change for 0 in 1 ways, that is by choosing nothing.
    
    for coin in coins:#Using a coin, one at a time
        for i in range(1,value+1):
            if(i>=coin):##Since it makes no sense to create change for value smaller than coin's denomination
                val = ways[i-coin]
                if(val!=1):
                    ways[i] += val
                else:
                    ways[i] += 1

    return ways[value]


#{ 
#Driver Code Starts.

def main():
    testcases=int(input())
    while(testcases>0):
        value=int(input())
        numberOfCoins=int(input())
        coins=[int(x) for x in input().strip().split()]
        print(numberOfWays(coins,numberOfCoins,value))
        testcases-=1

if __name__=="__main__":
    main()
    
#} Driver Code Ends
