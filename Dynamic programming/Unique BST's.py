#User function Template for python3

# Return the total number of BSTs possible with keys [1....N] inclusive.
def numTrees(n):
    mod = 10**9+7
    count = [0] * (n + 1)
    count[0] = 1

    for i in range(1, n + 1):
        for j in range(0, i):
            count[i] = (count[i] + (count[j] * count[i - j - 1]))%mod

    return count[n]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        n = int(input());
        print(numTrees(n))
# } Driver Code Ends
