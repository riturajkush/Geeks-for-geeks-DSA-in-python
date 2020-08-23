#User function Template for python3

# Graph (adj) is a default dict of type list
# V is the number of vertices in the graph


'''def DFSUtil(gr ,v, visited, res):
    visited[v] = True
    res.append(v)
    for i in gr[v]:
        if visited[i]==False:
            DFSUtil(i, visited)
    return res

def getTranspose(adj, V):
    graph = defultdict(list)
    for i in adj:
        for j in adj[i]:
            graph[j].append(i)
    return graph

def fillOrder(v, visited, stk, adj):
    visited[v] = True
    for i in adj[v]:
        if visited[i]==False:
            fillOrder(v, visited, stk, adj)
    stk = stk.append(v)


def countSCCs (adj, V):
    stk = []
    visited = [False]*V
    for i in range(V):
        if (visited[i]==False):
            fillOrder(i, visited, stk, adj)
    gr = getTranpose(adj, V)
    visited = [False]*V
    final = []
    while stk:
        i = stk.pop()
        if visited[i] == False:
            res = []
            final.append(DFSUtil(gr, i, visited, res))
    return len(final)'''
    
def dfs(g,src,finTime,vis):
    vis[src]=1
    for neigh in g[src]:
        if not vis[neigh]:
            dfs(g,neigh,finTime,vis)
    finTime+=[src]
 
def countSCCs(g,v):
    finTime=[]
    vis=[0]*v
    for i in range(v):
        if not vis[i]:
            dfs(g,i,finTime,vis)
    tg=defaultdict(list)
    for node in range(v):
        for neigh in g[node]:
            tg[neigh]+=[node]
    scc=0
    vis=[0]*v
    while finTime:
        cur=finTime.pop()
        if not vis[cur]:
            scc+=1
            dfs(tg,cur,[],vis)
    return scc
            



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        i += 2


from collections import defaultdict
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        print (countSCCs(graph, n))
        
# Contributed By: Pranay Bansal
# } Driver Code Ends
