def sumMatrix(n1, m1, n2, m2, arr1, arr2):
    #print(n1, n2, m1, m2)
    if(n1==n2) and (m1==m2):
        for i in range(0,n1):
            for j in range(0,m1):
                arr1[i][j] += arr2[i][j]
                print(arr1[i][j],end=" ")
    if (n1!=n2) or (m1!=m2):
        print("-1",end=" ")



#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        n1,m1=map(int,input().strip().split())
        arr1=[[0 for j in range(m1)] for i in range(n1)]
        line1=[int(x) for x in input().strip().split()]
        
       
        k=0
        for i in range(n1):
            for j in range (m1):
                arr1[i][j]=line1[k]
                k+=1
       
        k=0
       
        n2,m2=map(int,input().strip().split())
        arr2=[[0 for j in range(m2)] for i in range(n2)]
        line2=[int(x) for x in input().strip().split()]
        
       
        k=0
        for i in range(n2):
            for j in range (m2):
                arr2[i][j]=line2[k]
                k+=1
       
        k=0
       
       
       
        sumMatrix(n1, m1, n2, m2, arr1, arr2)
        print() 
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
