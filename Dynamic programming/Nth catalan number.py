from functools import lru_cache
@lru_cache(maxsize=None)
def f(x):
    return 1 if x==1 else x*f(x-1)
    
T = int(input())
while(T):
    n = int(input())
    print(f(2*n) // (f(n+1)*f(n)))
    T-=1
