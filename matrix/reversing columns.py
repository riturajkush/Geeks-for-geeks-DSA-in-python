#User function Template for python3

#arr1 is matrix
#n1 is rows
#m1 is cols
def reverseCol(n1, m1, arr):
    mid = m1//2
    for i in range(mid):
        for j in range(n1):
            arr[j][i], arr[j][m1-1-i] = arr[j][m1-1-i], arr[j][i]
    return arr



#{ 
#  Driver Code Starts
#Initial Template for Python 3


       
			
def main():
    T=int(input())
    while(T>0):
        n,m=map(int,input().split())
        mat=[[0 for j in range(m)] for i in range(n)]
        line1=[int(x) for x in input().strip().split()]
        
       
        k=0
        for i in range(n):
            for j in range (m):
                mat[i][j]=line1[k]
                k+=1
       
        k=0

        reverseCol(n, m, mat)
        
        for i in range(n):
            for j in range(m):
                print(mat[i][j],end=" ")
        print()
        
            
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
