
'''
g : adjacency list of graph
N : number of vertices

return a list containing the DFS traversal of the given graph
'''


        
def DfsUtil(v,visited,g,res):
    visited[v]=True
    res.append(v)
    for i in g[v]:
        if visited[i]==False:
            DfsUtil(i,visited,g,res)
    return res
def dfs(g,N):
    visited=[False]*(N)
    res = []
    return DfsUtil(0,visited,g,res)
        
          



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

#Contributed by : Nagendra Jha

#Graph Class:
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v): # add directed edge from u to v.
        self.graph[u].append(v)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N,E = map(int,input().strip().split())
        g = Graph(N)
        edges = list(map(int,input().strip().split()))

        for i in range(0,len(edges),2):
            u,v = edges[i],edges[i+1]
            g.addEdge(u,v) # add an undirected edge from u to v
            g.addEdge(v,u)

        res = dfs(g.graph,N)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()

# } Driver Code Ends
