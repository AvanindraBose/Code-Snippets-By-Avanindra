from collections import defaultdict,deque

class Graph:
    
    def BFS(self,node,par,adj,vis):
        dq = deque([[node,par]])
        vis[node] = True

        while len(dq):
            node,par = dq.popleft()

            for nbr in adj[node]:
                if not vis[nbr]:
                    vis[nbr] = True
                    dq.append([nbr,node])
                elif vis[nbr] == True and par != nbr:
                    #  cycle detected
                    print(nbr,par)
                    return True
        return False
 
    def create_adj_list(self,edges) -> dict[list]:
        adj_list = defaultdict(list)

        for u,v in edges: 
            adj_list[u].append(v)
            adj_list[v].append(u)

        return adj_list

if __name__ == "__main__":
    # LeetCode-style input
    graph = Graph()
    n = 6
    # Undirected Graph with a triangle cycle
    edges = [
        [0, 1],
        [0, 2],
        [1, 3],
        [2, 4],
        [3, 5],
        [4, 5],
        [1, 2],  # Added: creates cycle 0-1-2-0
    ]

    # Non-Cyclic Undirected Graph (Tree)
# 6 nodes, 5 edges → n - 1 = 5 ✅
    non_cyclic_edges = [
        [0, 1],
        [0, 2],
        [1, 3],
        [2, 4],
        [3, 5],
    ]

    adj = graph.create_adj_list(edges)
    vis = [False]*(n)
    iscycle = graph.BFS(0,-1,adj,vis)

    print(iscycle)

    adj_1 = graph.create_adj_list(non_cyclic_edges)
    vis_1 = [False]*(n)
    iscycle1 = graph.BFS(0,-1,adj_1,vis_1)

    print(iscycle1)