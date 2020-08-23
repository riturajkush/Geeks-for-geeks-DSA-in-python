#User function Template for python3

#mat is matrix
#n1 is rows
#m1 is cols
#x is element to search
def search(n1, m1, mat, x):

    row=0 
    col=m1-1
    while(row<n1 and col>=0):
        key = mat[row][col]
        if (key==x):
            return 1
        elif (key>x):
            col -= 1
        else:
            row += 1
    return 0



#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():
    T=int(input())
    while(T>0):
        n,m=map(int,input().split())
        mat=[[0 for j in range(m)] for i in range(n)]
        line1=[int(x) for x in input().strip().split()]
        x=int(input())
       
        k=0
        for i in range(n):
            for j in range (m):
                mat[i][j]=line1[k]
                k+=1
       
        print(search(n, m, mat,x))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
