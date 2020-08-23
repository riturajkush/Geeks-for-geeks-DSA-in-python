#User function Template for python3


##Complete this function
def possibleWords(a,N):
    #print(a, N)
    vals = []
    for i in range(N):
        if (a[i]==2):
            vals.append("abc")
        elif (a[i]==3):
            vals.append("def")
        elif (a[i]==4):
            vals.append("ghi")
        elif (a[i]==5):
            vals.append("jkl")
        elif (a[i]==6):
            vals.append("mno")
        elif (a[i]==7):
            vals.append("pqrs")
        elif (a[i]==8):
            vals.append("tuv")
        elif (a[i]==9):
            vals.append("wxyz")
        else:
            continue
    #print(vals)
    #return vals
    if(N==1):
        return list(vals[0])
    i = 1
    res = list(vals[0])
    ans = genComb(vals, N, i, res)
    return ans
    
def genComb(vals, N, i, res):
    if (i==N):
        return res
    ans = []
    for j in range(len(res)):
        sec_val = vals[i]
        for k in range(len(sec_val)):
            ans.append(res[j]+sec_val[k])
    res = ans
    return genComb(vals, N, i+1, res)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        
        res = possibleWords(a,N)
        for i in range (len (res)):
            print (res[i], end = " ") 
        
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
