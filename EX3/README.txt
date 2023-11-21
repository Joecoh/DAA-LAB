Decrease and Conquer - Topological Sorting

Topological sorting is a common problem in graph theory. It involves linearly ordering the vertices of a directed acyclic graph (DAG) in such a way that for every directed edge (u, v), vertex u comes before vertex v in the ordering. This ordering is called a "topological order."

Decrease and conquer is an approach where the problem is reduced to a smaller instance of the same problem. In the case of topological sorting, the decrease and conquer strategy involves removing a vertex with no incoming edges (in-degree of 0) and its associated edges until the graph is empty.

we create a directed graph with six vertices and add edges between them. The topological_sort method initiates the topological sorting process, and the result is printed.

The time complexity of this implementation is O(V + E), where V is the number of vertices and E is the number of edges in the graph. The decrease and conquer approach involves repeatedly selecting a vertex with in-degree 0, removing it and its outgoing edges, and updating the in-degrees of the remaining vertices. The process continues until all vertices are processed.