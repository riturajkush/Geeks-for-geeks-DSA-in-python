#User function Template for python3


#r is rows
#c is cols
#mat is matrx
#print it in this function after modifying it
def booleanMatrix(r, c, mat):
    row = set()
    col = set()
    for i in range(0,r):
        for j in range(0,c):
            if(mat[i][j]==1):
                row.add(i)
                col.add(j)
    for i in row:
        mat[i] = [1]*c
    for j in col:
        for i in range(r):
            mat[i][j] = 1
    
    for i in range(0,r):
        for j in range(0,c):
            print(mat[i][j], end=" ")
        print()




#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        r,c=map(int,input().split())
        
        
        mat=[]
        for i in range(r):
            line=[int(x) for x in input().strip().split()]
            mat.append(line)

        booleanMatrix(r, c, mat)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
