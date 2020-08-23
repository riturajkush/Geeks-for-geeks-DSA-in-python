def sorting(arr1, arr2, n, m):
    '''a = set(arr1)
    b = set(arr2)
    c = a.difference(b)
    c = sorted(c)'''
    c= []
    for i in arr1:
        if(i not in arr2):
            c.append(i)
    c = sorted(c)
    dic = dict()
    lst = []
    for i in arr1:
        if(i in arr2) and (i not in c):
            if(i in dic):
                dic[i] += 1
            else:
                dic[i] = 1
    #print(dic)
                
    for i in arr2:
        for j in range(dic[i]):
            lst.append(i)
    for i in lst:
        print(i,end=" ")
    for j in c:
        print(j,end=" ")
    print()
    
            
            
t = int(input())
for i in range(0,t):
    n,m = list(map(int,input().strip().split()))
    arr1 = list(map(int,input().strip().split()))
    arr2 = list(map(int,input().strip().split()))
    sorting(arr1, arr2, n, m)
