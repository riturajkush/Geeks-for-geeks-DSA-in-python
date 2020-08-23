for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    dic = {}    #stores how many subarray with particular sum we have found till now
    curr_sum = 0
    count=0
    for i in range(n):
        curr_sum+=arr[i]
        print("curr_sum", curr_sum)
        print("@@@",dic)
        if curr_sum == 0: # we found subarray starting from the index 0 to current i
            count+=1
            print("1st if", count)
        if curr_sum in dic:
            print("curr_sum in if",curr_sum)
            count+=dic[curr_sum]    #adding all the subaarays with this sum found till now
            print("2nd if", count)
        dic[curr_sum] =dic.get(curr_sum,0) + 1 
        print("###",dic)
    print(count)
        
