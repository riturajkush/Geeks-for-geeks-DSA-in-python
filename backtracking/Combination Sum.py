#{ 
#Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


 # } Driver Code Ends

#User function Template for python3

ans = []
def combinationalSum(A, B):
    global ans
    ans = []
    A = list(set(A))
    A.sort()
    #print(A)
    calAns(A, B, [], 0)
    return ans
    
def calAns(A, B, so_far, start):
    global ans
    #print(so_far)
    if (B==0):
        ans.append(so_far)
        return
    if (B<0):
        return
    for i in range(start, len(A)):
        #print(A)
        calAns(A, B-A[i], so_far+[A[i]], i)


#{ 
#Driver Code Starts.


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        s = int(input())
        result = combinationalSum(a,s)
        if(not len(result)):
            print("Empty")
            continue
        for i in range(len(result)):
            print("(", end="")
            size = len(result[i])
            for j in range(size - 1):
                print(result[i][j], end=" ")
            if (size):
                print(result[i][size - 1], end=")")
            else:
                print(")", end="")
        print()

#} Driver Code Ends
