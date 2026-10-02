import matplotlib.pyplot as plt
from collections import defaultdict
from collections import deque

#  TC -> O(V+E)
#  SC -> O(V+E)

class Graph():

    def create_adj_list(self,n,edges):
        #  given a list of edges I need to convert it into an Adjacency List!!
        adj = defaultdict(list)
        for u,v in edges :
            adj[u].append(v)

        return adj


    def BFS(self,node,adj,vis,result):
        dq = deque([node])

        while len(dq):
            new_node = dq.popleft()
            result.append(new_node)

            for nbr in adj[new_node]:
                if not vis[nbr]:
                    vis[nbr] = True
                    dq.append(nbr)

if __name__ == "__main__":
    # LeetCode-style input
    graph = Graph()
    n = 6
    # directed Graph Example
    edges = [
        [0, 1],
        [0, 2],
        [1, 3],
        [2, 4],
        [3, 5],
        [4, 5],
    ]

    adj = graph.create_adj_list(n,edges)

    print(adj)
    vis = [False]*(n)
    result = []
    graph.BFS(0,adj,vis,result)

    print(result)