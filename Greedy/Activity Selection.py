#User function Template for python3
def maximumActivities(n,start,end):
    b = []
    for i in range(n):
        b.append([end[i], start[i]])
    b = sorted(b)
    c = 1
    t = b[0][0]
    #print(b)
    for i in range(1, n):
        if b[i][1] >= t:
            #print(t)
            c += 1
            t = b[i][0]
    
    return c
            
        



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        print(maximumActivities(n,start,end))
# } Driver Code Ends
