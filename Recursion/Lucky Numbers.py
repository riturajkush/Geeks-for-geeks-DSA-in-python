#User function Template for python3

def isLucky(n):
    counter = 2
    if(calcLucky(counter, n)):
        return 0
    else:
        return 1

def calcLucky(counter, n):
    if (counter>n):
        return False
    if (n%counter==0):
        return True
    np = n
    np = np - np//counter
    counter += 1
    return calcLucky(counter, np)



#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
c=2
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        c=2
        
        n=int(input())
        print(isLucky(n))
        
# } Driver Code Ends
