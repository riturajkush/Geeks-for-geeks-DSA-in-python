import collections
def rotOranges(mat, r, c):
    count = 0
    que = collections.deque()
    for i in range(r):
        for j in range(c):
            if (mat[i][j]==1):
                count += 1
            elif (mat[i][j]==2):
                que.append((i,j))
    res = 0
    #print(count)
    #print(que)
    while(que):
        for k in range(len(que)):
            #print(i,j)
            i,j = que.popleft()
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                #print(x,y)
                if (0<=x<r and 0<=y<c and mat[x][y]==1):
                    mat[x][y]=2
                    count -= 1
                    que.append((x,y))
        #print(que)
        res += 1
    if (count==0):
        return max(0,res-1)
    else:
        return -1
                
                



#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        rc=input().split() #row and column
        r=int(rc[0])    
        c=int(rc[1])
        l=list(map(int, input().strip().split(' ')))
        
        mat=[]
        for i in range(r):
            mat.append([])
            for j in range(c):
                mat[i].append([])
                mat[i][j]=l.pop()
                
        print(rotOranges(mat,r,c))
# } Driver Code Ends
