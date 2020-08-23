def minimumpages(arr, n, m):

l = 0
r = n-1
num = 2
while(num<2):
    dividebooks(arr, l, r, n)
    num = num + 1

def dividebooks(arr, l, r, n):
    if (l<=r):
        mid = l + (r-l)//2
        

t = int(input())
for i in range(0,t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    m = int(input())
    print(minimumpages(arr, n, m))
