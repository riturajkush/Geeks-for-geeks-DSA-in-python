def count_ways(n):
    ways = [0]*(n+1)
    ways[0] = 1
    for i in range(3,n+1):
        ways[i] += ways[i-3]
    for i in range(5,n+1):
        ways[i] += ways[i-5]
    for i in range(10, n+1):
        ways[i] += ways[i-10]
    print(ways[n])



t = int(input())
for i in range(t):
    n = int(input())
    count_ways(n)
