#User function Template for python3
def DFSRec(g, s, visited, parent):
    visited[s] = 1
    for u in g[s]:
        if(visited[u]==0):
            if(DFSRec(g, u, visited, s)==1):
                return 1
        elif (u!=parent):
            return 1
    return 0


def isCyclic(g,n):
    visited = [0]*n
    for i in range(n):
        if(visited[i]==0):
            if(DFSRec(g, i, visited, -1)==1):
                return 1
    return 0



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from collections import defaultdict

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
        print(isCyclic(g.graph,N))
# } Driver Code Ends
