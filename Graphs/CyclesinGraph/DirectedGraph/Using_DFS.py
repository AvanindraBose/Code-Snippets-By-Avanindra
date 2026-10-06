from collections import defaultdict

class Graph:
    def DFS(self,node,adj,vis) -> bool:

        vis[node] = True

        for nbr in adj[node]:
            if vis[nbr] == False:
                self.DFS(nbr,adj,vis)
            elif vis[nbr] == True:
                # cycle detected
                return True

        return False

    def create_adj_list(self,edges) -> dict[list]:
        adj_list = defaultdict(list)

        for u,v in edges: 
            adj_list[u].append(v)

        return adj_list

if __name__ == "__main__":
    # LeetCode-style input
    graph = Graph()
    n = 6
    # Undirected Graph with a triangle cycle
    # Directed Graph with a cycle
# Cycle: 0 → 1 → 2 → 0
    edges = [
        [0, 1],
        [0, 2],
        [1, 3],
        [2, 4],
        [3, 5],
        [4, 5],
        [1, 2],   # Added: creates cycle 0 → 1 → 2 → 0
        [2, 0],   # Needed to close the cycle in a directed graph
    ]

    # Directed Acyclic Graph (DAG)
    # 6 nodes, 5 edges → no cycles
    non_cyclic_edges = [
        [0, 1],
        [0, 2],
        [1, 3],
        [2, 4],
        [3, 5],
    ]

    adj = graph.create_adj_list(edges)
    vis = [False]*(n)
    iscycle = graph.DFS(0,adj,vis)

    print(iscycle)

    adj_1 = graph.create_adj_list(non_cyclic_edges)
    vis_1 = [False]*(n)
    iscycle1 = graph.DFS(0,adj_1,vis_1)

    print(iscycle1)