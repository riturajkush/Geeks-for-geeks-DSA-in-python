#User function Template for python3

#Complete this function
def winner(arr,n):
    d = {}
    for i in arr:
        d[i] = 0
    for i in arr:
        d[i] += 1
    maxn = max(d.values())
    res = 0
    for m in sorted(list(d.keys())):
        if(d[m]==maxn):
            print(m,maxn)
            break
    
        
    
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3


    

def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=input().strip().split()
        
        winner(arr,n)
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
