#User function Template for python3

# Function to construct and return cost of MST for a graph
# represented using adjacency matrix representation
'''
V: nodes in graph
E: number of edges in graph
graph: adjacency matrix, graph[i][j]=weight, if edge exits , else float("inf").
'''
def spanningTree(V, E, graph):
    stk = [1]
    ct = 1
    cost = 0
    while(ct<=V-1):
        res = float("inf")
        for i in range(0,len(stk)):
            if(stk[i]!=-100):
                if len(set(graph[stk[i]-1]))==1:
                    stk[i] = -100
                else:
                    for j in range(V):
                        #print("stk[i],j",stk[i]-1,j)
                        if (graph[stk[i]-1][j]!=float("inf") and j+1 not in stk):
                            res = min(res,graph[stk[i]-1][j])
                        if (res==graph[stk[i]-1][j]):
                            m,n = stk[i]-1,j
        stk.append(n+1)
        ct += 1
        #print("stk",stk)
        cost += res
        #print("cost",cost)
        graph[m][n] = float("inf")
        graph[n][m] = float("inf")
        #print(graph)
    return cost
                
                



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        graph = [[float("inf") for i in range(V)] for i in range(V)]
        for i in range(0,len(info),3):
            u,v,w = info[i]-1,info[i+1]-1,info[i+2]
            graph[u][v] = w
            graph[v][u] = w
        print(spanningTree(V,E,graph))
# } Driver Code Ends
