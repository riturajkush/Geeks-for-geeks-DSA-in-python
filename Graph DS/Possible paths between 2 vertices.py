#User function Template for python3


def countPath(g,s,d):
    '''
    :param g: given adjacency list of graph
    :param s: source
    :param d: destination
    :return: no. of path
    '''
    visited = [False]*(len(graph)+10)
    #print(visited)

    pathCount = [0]
    countPathUtil(graph, s, d, visited, pathCount)
    #print(graph)

    return pathCount[0]
    
def countPathUtil(graph, u, d, visited, pathCount):    
    visited[u] = True
    
    if u == d:
        pathCount[0] += 1
    
    else:
    
        for i in graph[u]:
            #print(i)
            if not visited[i]:
                countPathUtil(graph, i, d, visited, pathCount)
    
    visited[u] = False



#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

from collections import defaultdict

def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        # graph[arr[i + 1]].append(arr[i])
        i += 2



if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        s,d=list(map(int, input().strip().split()))
        print(countPath(graph,s,d))
# } Driver Code Ends
