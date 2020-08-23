#User function Template for python3

# Function to construct and return cost of MST for a graph
# represented using adjacency matrix representation
'''
V: nodes in graph
E: number of edges in graph
graph: adjacency matrix, graph[i][j]=weight, if edge exits , else float("inf").
'''
def spanningTree(V, E, graph):
    res = 0
    key = [float("inf")]*V
    key[0] = 0
    mSet = [False]*V
    
    for count in range(V):
        u = -1
        for i in range(V):
            if (not mSet[i] and (u==-1 or key[i]<key[u])):
                u = i
        mSet[u] = True
        res += key[u]
        for v in range(V):
            if (graph[u][v]!=0 and not mSet[v]):
                key[v]=min(key[v],graph[u][v])
    return res
                
                



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
