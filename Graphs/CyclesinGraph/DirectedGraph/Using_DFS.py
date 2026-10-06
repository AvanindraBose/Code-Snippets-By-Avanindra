from collections import defaultdict

class Graph:
    def DFS(self,node,adj,vis,curr_recursion) -> bool:

        vis[node] = True
        curr_recursion[node] = True

        for nbr in adj[node]:
            if vis[nbr] == False:
                if self.DFS(nbr,adj,vis,curr_recursion):
                    return True
            elif curr_recursion[nbr] == True:
                # cycle detected
                return True
        curr_recursion[node] = False
        return False

    def create_adj_list(self,edges) -> dict[list]:
        adj_list = defaultdict(list)

        for u,v in edges: 
            adj_list[u].append(v)

        return adj_list

if __name__ == "__main__":
    # LeetCode-style input
    graph = Graph()

    # Directed Graph with Multiple Components
    #
    # Component 1 (nodes 0-5): contains cycle 0 → 1 → 2 → 0
    # Component 2 (nodes 6-9): a DAG (no cycle)
    # Component 3 (nodes 10-12): contains cycle 10 → 11 → 12 → 10
    # Component 4 (nodes 13-14): isolated node + tiny DAG
    #
    # Total nodes = 15
    edges = [
        # ---- Component 1: has cycle 0 → 1 → 2 → 0 ----
        [0, 1],
        [0, 2],
        [1, 3],
        [2, 4],
        [3, 5],
        [4, 5],
        [1, 2],
        [2, 0],        # closes directed cycle 0 → 1 → 2 → 0

        # ---- Component 2: DAG (no cycle) ----
        [6, 7],
        [6, 8],
        [7, 9],
        [8, 9],

        # ---- Component 3: has cycle 10 → 11 → 12 → 10 ----
        [10, 11],
        [11, 12],
        [12, 10],

        # ---- Component 4: tiny DAG ----
        [13, 14],
    ]

    n = 15# total number of nodes (0 .. 14)

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
    # My Logic will fail for multiple Components of Graph!
    iscycle = False
    vis = [False]*(n)
    curr_recursion = [False]*(n)

    for i in range(n):
        if vis[i] == False :
            if graph.DFS(i,adj,vis,curr_recursion):
                iscycle = True
                break

    print(iscycle)