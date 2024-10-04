## set recursion size for stack
import sys
sys.setrecursionlimit(10000000)

## [Applications of Depth First Search](https://cp-algorithms.com/graph/depth-first-search.html)
    Find any path in the graph from source vertex  to all vertices.

    Find lexicographical first path in the graph from source  to all vertices.

    Check if a vertex in a tree is an ancestor of some other vertex:

        At the beginning and end of each search call we remember the entry and exit "time" of each vertex. Now you can find the answer for any pair of vertices  in : vertex  is an ancestor of vertex  if and only if  and .

    Find the lowest common ancestor (LCA) of two vertices.

    Topological sorting:

        Run a series of depth first searches so as to visit each vertex exactly once in  time. The required topological ordering will be the vertices sorted in descending order of exit time.

    Check whether a given graph is acyclic and find cycles in a graph. (As mentioned above by counting back edges in every connected components).

    Find [strongly connected components](algorithm\dfs\SSC.py) in a directed graph:

        First do a topological sorting of the graph. Then transpose the graph and run another series of depth first searches in the order defined by the topological sort. For each DFS call the component created by it is a strongly connected component.

    [Find bridges in an undirected graph](algorithm\dfs\findBridge.py):

        First convert the given graph into a directed graph by running a series of depth first searches and making each edge directed as we go through it, in the direction we went. Second, find the strongly connected components in this directed graph. Bridges are the edges whose ends belong to different strongly connected components.

## 

Tarjan for search distance in tree algorithm\tree\lca\tarjan.py