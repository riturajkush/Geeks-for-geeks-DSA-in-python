def scs(m,n,X,Y):
 
    L = [[None]*(n+1) for i in range(m+1)] 
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 

    return m+n-L[m][n] 

t = int(input())
for i in range(t):
    s1, s2 = [str(x) for x in input().split()]
    n1 = len(s1)
    n2 = len(s2)
    print(scs(n1, n2, s1, s2))
