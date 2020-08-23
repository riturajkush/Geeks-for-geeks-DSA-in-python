t = int(input())
for i in range(t):
    n = int(input())
    i = 0
    b = 1
    a = 0
    c = 0
    while(i!=n):
        print(b,end=" ")
        c = a+b
        a = b
        b = c
        i += 1
    print("")
