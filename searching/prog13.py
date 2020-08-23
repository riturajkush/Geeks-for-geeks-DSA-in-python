def Searchnum(A, l, r):
    if (l<=r):
        mid = l + (r-l)//2
    if (mid>0 and A[mid]==A[mid-1]) or (mid<(n-1) and A[mid]==A[mid+1]):
        return A[mid]
    if (A[0]+mid == A[mid]):
        return Searchnum(A, mid+1, r)
    else:
        return Searchnum(A, l, mid-1)

t = int(input())
for i in range(0,t):
    n = int(input())
    A = list(map(int, input().strip().split()))
    l = 0
    r = n-1
    number = Searchnum(A, l, r)
    count = A[0] + n - A[n-1]
    print(number, count)
