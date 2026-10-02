import matplotlib.pyplot as plt
from collections import defaultdict

#  TC -> O(V+E)
#  SC -> O(V+E)
class Graph():
    def plot_graph(self,n, edges):
        """Plot an undirected graph given n nodes and a list of edges."""
        fig, ax = plt.subplots(figsize=(8, 8))

        # Place nodes on a circle
        import math
        positions = {}
        for i in range(n):
            angle = 2 * math.pi * i / n
            positions[i] = (math.cos(angle), math.sin(angle))

        # Draw edges
        for u, v in edges:
            x1, y1 = positions[u]
            x2, y2 = positions[v]
            ax.plot([x1, x2], [y1, y2], color="gray", linewidth=1, zorder=1)

        # Draw nodes
        for i in range(n):
            x, y = positions[i]
            ax.scatter(x, y, s=500, color="tab:blue", zorder=2)
            ax.text(x, y, str(i), color="white", ha="center", va="center",
                    fontsize=12, zorder=3)

        ax.set_title("Graph")
        ax.set_aspect("equal")
        ax.axis("off")
        plt.tight_layout()
        plt.show()

    def create_adj_list(self,n,edges):
        #  given a list of edges I need to convert it into an Adjacency List!!
        adj = defaultdict(list)
        for u,v in edges :
            adj[u].append(v)

        return adj

    def DFS(self,node,adj,vis,result):

        vis[node] = True
        result.append(node)

        for nbr in adj[node]:
            if not vis[nbr] :
                self.DFS(nbr,adj,vis,result)

        return
    
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

    # graph.plot_graph(n, edges)
    adj = graph.create_adj_list(n,edges)

    print(adj)
    vis = [False]*(n)
    result = []
    graph.DFS(0,adj,vis,result)

    print(result)

    