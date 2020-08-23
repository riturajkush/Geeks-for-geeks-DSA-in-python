def numcontaining(arr, n):
    set_num = {"1","2","3"}
    lst = []
    for i in arr:
        count = False
        for j in i:
            #print("i","j",i,j)
            if(j in set_num):
                #print("j",j)
                count = True
            else:
                count = False
                break
        if(count):
            lst.append(i)
    if (len(lst)==0):
        print("-1",end=" ")
    else:
        for i in lst:
            print(i,end=" ")
    #print(lst)


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(str, input().split()))
    numcontaining(arr, n)
    print()

