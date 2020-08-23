#User function Template for python3

def largestNum(n,s):
    if (s == 0) : 
        if(n == 1) : 
            return 0  
        else : 
            return -1 
  
    if (s > 9 * n) : 
        return -1 

    res = [0] * n

    for i in range(0, n) : 
        if (s >= 9) : 
            res[i] = 9
            s = s - 9
        else : 
            res[i] = s 
            s = 0
    final = ""  
    for i in range(0, n) : 
        final += str(res[i])
    return final
            
    
    



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
        n,s = map(int,input().strip().split())
        print(largestNum(n,s))
# } Driver Code Ends
