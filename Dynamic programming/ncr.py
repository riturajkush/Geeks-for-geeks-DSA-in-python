#User function Template for python3

# Returns value of Binomial Coefficient C(n, r) under modulo
def nCr(n, r):
    if(n<r):
        return 0
    if(n==r):
        return 1
    mod = (10**9+7)
    if(n-r>r):
        val = n-r
    else:
        val = r
    nt = 1
    for i in range(val+1, n+1):
        nt = ((nt) * (i))
    dt = 1
    for i in range(2,n-val+1):
        dt = ((dt) * (i))
    #print(nt, dt)
    return ((nt)//(dt))%mod



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,r = map(int,input().strip().split())
        print(nCr(n,r))
# } Driver Code Ends
