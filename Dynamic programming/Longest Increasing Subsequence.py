#User function Template for python3
def ceilIndex(tail, l, r, x):
    while(l<r):
        m = l+(r-l)//2
        if(tail[m]>=x):
            r = m
        else:
            l = m+1
    return r
    
def longestSubsequence(a,n):
    # code here
    # return length of the longest increasing sub sequence
    tail = []
    tail.append(a[0])
    length = 1
    for i in range(1,n):
        if(a[i]>tail[length-1]):
            tail.append(a[i])
            length += 1
        else:
            c = ceilIndex(tail, 0, length-1, a[i])
            tail[c] = a[i]
    return length








#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        print(longestSubsequence(a,n))
# } Driver Code Ends
