#User function Template for python3

#Complete this function
def isIsogram(s):
    table = [0]*26
    for i in s:
        table[ord(i)-97] += 1
    for i in range(26):
        if (table[i]>1):
           return False
    return True

#{ 
#  Driver Code Starts
#Initial Template for Python 3




def main():
    T=int(input())
    
    while(T>0):
        
        s=input()
        if isIsogram(s) is True:
            print(1)
        else:
            print(0)
        T-=1


if __name__=="__main__":
    main()
# } Driver Code Ends
