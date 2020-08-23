# Your task is to complete this function
# Function should return Topologically Sorted List
# Graph(adj) is a defaultict of type List
# n is no of edges
def DFSUtil(v,visited,g,res):
    #print("@@",v)
    visited[v] = True
    for i in g[v]:
        if (visited[i]==False) :
            res = DFSUtil(i, visited,g,res)
    res.append(v)
    #print("##",res)
    return res

def topoSort(n, adj):
    #print(adj)
    visited=[False]*(n)
    res = []
    for i in range(n):
        if(visited[i]==False):
            res = DFSUtil(i,visited,adj,res)
    final = [0]*n
    for i in range(n):
        final[i] = res[n-1-i]
    return final
    





#{ 
#  Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
def creategraph(e, n, arr, graph):
    i = 0
    while i<2*e:
        graph[arr[i]].append(arr[i+1])
        i+=2
        
def check(graph, N, res):
	map=[0]*N
	for i in range(N):
		map[res[i]]=i
	for i in range(N):
		for v in graph[i]:
			if map[i] > map[v]:
				return False
	return True

from collections import defaultdict
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, N, arr, graph)
        res = topoSort(N, graph)
        
        if check(graph, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends
