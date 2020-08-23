# Your task is to complete this function
# Function should return True/False or 1/0
# Graph(graph) is a defaultict of type List
# n is no of Vertices
def isCyclicUtil(i, graph, visited, recst):
    visited[i] = True
    recst[i] = True
    for u in graph[i]:
        if((visited[u]==False) and isCyclicUtil(u, graph, visited, recst)):
            return True
        elif(recst[u]==True):
            return True
    recst[i] = False
    return False
    
    
def isCyclic(n, graph):
    visited = [False]*n
    recst = [False]*n
    for i in range(n):
        if(visited[i]==False):
            if(isCyclicUtil(i, graph, visited, recst)==True):
                return True
    return False
        



#{ 
#  Driver Code Starts

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
        if isCyclic(n, graph):
            print(1)
        else:
            print(0)
# } Driver Code Ends
