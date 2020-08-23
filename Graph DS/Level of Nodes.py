#User function Template for python3
#import queue
from collections import deque
def levels(g,n,x):
    Q = deque([])
    
    Q.append([0, 0])
    v = [0 for i in range(n)]
    v[0] = 1
    while len(Q):
        curr = Q.popleft()
        v[curr[0]] = 1
        if curr[0] in g:
            for i in g[curr[0]]:
                if i == x:
                    return curr[1]+1
                if not(v[i]):   
                    Q.append([i, curr[1]+1])
    return -1
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from collections import defaultdict
import queue

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
        for i in range(E):
            u,v = map(int,input().strip().split())
            g.addEdge(u,v) # add an directed edge from u to v
            g.addEdge(v,u) # add an directed edge from u to v
        x=int(input())
        print(levels(g.graph,N,x))

# } Driver Code Ends
