from collections import deque

# Created by Lucy Antonescu and Kendall Mamich

#Graph data structure class represented as a adjacency list
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def addEdge(self, u, v):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)


# G is the graph data structure being passed in
def breathFirstSearch(G):
    mark = {vertex: 0 for vertex in G.adjacency_list}
    count = 0
    bfs = []

    for vertex in G.adjacency_list:
        if mark[vertex] == 0:
            count += 1
            queue = deque([vertex])
            mark[vertex] = count

            while queue:
                current = queue.popleft()
                bfs.append(current)

                for neighbor in G.adjacency_list.get(current, []):
                    if mark[neighbor] == 0:
                        count += 1
                        mark[neighbor] = count
                        queue.append(neighbor)
    return bfs

# G is the graph data structure being passed in
def depthFirstSearch(G):
    mark = {vertex: 0 for vertex in G.adjacency_list}
    dfs = []
    stack = []

    def dfsVisit(vertex):
        mark[vertex] = 1
        dfs.append(vertex)

        for neighbor in G.adjacency_list.get(vertex, []):
            if mark[neighbor] == 0:
                dfsVisit(neighbor)
        stack.append(vertex)

    for vertex in G.adjacency_list:
        if mark[vertex] == 0:
            dfsVisit(vertex)
    stack.reverse()
    return (dfs, stack)

# G is the graph data structure being passed in. It will be treated as a digraph.
def topologicalSortDFS(G):
    dfs, topologicalSort = depthFirstSearch(G)
    return(topologicalSort)


if __name__ == "__main__":
    graph1 = Graph()
    graph2 = Graph()
    graph3 = Graph()
    # Graph with eight vertices and twelve edges
    edges1 = [(0,1),(0,2),(1,3),(1,4),(2,4),(3,5),(4,5),(4,6), (5,7),(6,7),(5,2),(7,3)]
    # Graph with nine vertices and twelve edges
    edges2 = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (3, 5), (4, 6), (5, 6), (6, 7), (7, 8), (5, 8), (2, 3)]
    # Graph with eight vertices and seven edges
    edges3 = [(0,1), (0,2), (0,3), (1,4), (1,5), (2,6), (3,7)]
    
    for u, v in edges1:
        graph1.addEdge(u, v)

    for u, v in edges2:
        graph2.addEdge(u, v)

    for u, v in edges3:
        graph3.addEdge(u, v)

    # BFS examples
    bfs1 = breathFirstSearch(graph1)
    bfs2 = breathFirstSearch(graph2)
    bfs3 = breathFirstSearch(graph3)
    print(f"BFS Traversal Order for graph 1: {bfs1}")
    print(f"BFS Traversal Order for graph 2: {bfs2}")
    print(f"BFS Traversal Order for graph 3: {bfs3}\n")

    # DFS examples
    dfs1,stack1 = depthFirstSearch(graph1)
    dfs2,stack2 = depthFirstSearch(graph2)
    dfs3,stack3 = depthFirstSearch(graph3)
    print(f"DFS Traversal Order for graph 1: {dfs1}")
    print(f"DFS Traversal Order for graph 2: {dfs2}")
    print(f"DFS Traversal Order for graph 3: {dfs3}\n")

    # Topological Sort DFS examples:
    tsdfs1 = topologicalSortDFS(graph1)
    tsdfs2 = topologicalSortDFS(graph2)
    tsdfs3 = topologicalSortDFS(graph3)
    print(f"Topological sort DFS for graph 1: {tsdfs1}")
    print(f"Topological sort DFS for graph 2: {tsdfs2}")
    print(f"Topological sort DFS for graph 3: {tsdfs3}")