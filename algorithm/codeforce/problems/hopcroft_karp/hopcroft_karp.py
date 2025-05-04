from collections import deque

class HopcroftKarp:
    def __init__(self, graph):
        """
        Initialize the Hopcroft-Karp algorithm with a bipartite graph.
        The graph should be a dictionary where keys are vertices in one partition (U),
        and values are lists of vertices in the other partition (V) that they are connected to.
        """
        self.graph = graph
        self.U = set(graph.keys())
        self.V = set()
        for neighbors in graph.values():
            self.V.update(neighbors)
        self.pair_U = {u: None for u in self.U}
        self.pair_V = {v: None for v in self.V}
        self.dist = {}
    
    def bfs(self):
        """Breadth-first search to find the layered graph."""
        queue = deque()
        
        # Initialize distances for U vertices
        for u in self.U:
            if self.pair_U[u] is None:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')
        
        self.dist[None] = float('inf')
        
        while queue:
            u = queue.popleft()
            if self.dist[u] < self.dist[None]:
                for v in self.graph[u]:
                    if self.dist[self.pair_V[v]] == float('inf'):
                        self.dist[self.pair_V[v]] = self.dist[u] + 1
                        queue.append(self.pair_V[v])
        #print(self.dist,self.pair_U,self.pair_V)
        return self.dist[None] != float('inf')
    
    def dfs(self, u):
        """Depth-first search to find augmenting paths."""
        if u is not None:
            for v in self.graph[u]:
                if self.dist[self.pair_V[v]] == self.dist[u] + 1:
                    if self.dfs(self.pair_V[v]):
                        self.pair_U[u] = v
                        self.pair_V[v] = u
                        return True
            self.dist[u] = float('inf')
            return False
        return True
    
    def max_matching(self):
        """Find the maximum matching in the bipartite graph."""
        matching = 0
        while self.bfs():
            for u in self.U:
                if self.pair_U[u] is None:
                    if self.dfs(u):
                        matching += 1
        return matching
    
    def get_matching(self):
        """Return the actual matching pairs as a dictionary."""
        return {u: v for u, v in self.pair_U.items() if v is not None}


# Example usage:
if __name__ == "__main__":
    # Example bipartite graph
    graph = {
        'u1': ['v1', 'v2'],
        'u2': ['v2', 'v3'],
        'u3': ['v1', 'v3'],
        'u4': ['v4'],
    }
    
    hk = HopcroftKarp(graph)
    max_matching = hk.max_matching()
    print(f"Maximum matching size: {max_matching}")
    print("Matching pairs:", hk.get_matching())


# Explanation:
# Initialization: The algorithm takes a bipartite graph represented as a dictionary where keys are vertices in one partition (U) and values are their neighbors in the other partition (V).

# BFS (Breadth-First Search):

# Constructs a layered graph starting from unmatched vertices in U

# Calculates distances to find the shortest augmenting paths

# DFS (Depth-First Search):

# Finds augmenting paths using the layered graph

# Updates the matching when an augmenting path is found

# Max Matching:

# Repeatedly performs BFS and DFS until no more augmenting paths exist

# Returns the size of the maximum matching

# Get Matching:

# Returns the actual pairs of vertices that form the matching

# The algorithm runs in O(√VE) time complexity, where V is the number of vertices and E is the number of edges, making it one of the most efficient algorithms for bipartite matching.

# You can modify the input graph to test with different bipartite graphs. The example provided has a maximum matching of 4.