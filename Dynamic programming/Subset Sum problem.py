def func(arr, n, sum, i):
    if sum==0:
        return True
    if sum<0 or i>=n:
        return False
    return func(arr,n,sum-arr[i],i+1) or func(arr,n,sum,i+1)
    
for i in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    max=sum(lst)
    req=max//2
    if func(lst,n,req,0) and max%2==0:
        print("YES")
    else:
        print("NO")
