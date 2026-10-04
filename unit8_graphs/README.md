# Unit 8 Discussion: Breadth-First Search

## Overview

This assignment implemented Breadth-First Search (BFS) for a streaming-catalog graph. Titles were represented as nodes, and connections represented shared genres, cast members, or viewer-rating relationships.

## Learning Objectives

- Represented a graph with an adjacency list
- Implemented queue-based BFS
- Tracked visited nodes to prevent repeated work in cyclic graphs
- Analyzed level-by-level graph traversal and edge cases
- Connected graph traversal to recommendations in a streaming catalog

## Requirements

1. Created and displayed an adjacency-list graph with at least six nodes.
2. Implemented BFS and displayed its traversal order.
3. Added a graph connection and displayed the updated traversal.
4. Demonstrated missing-start, empty-graph, and single-node cases.
5. Explained the BFS and DFS trade-offs in a real-world context.

## Implementation Summary

**Author: Firaz Khan**

The `bfs` function used a `deque` as a first-in, first-out queue. It marked the start node as visited, removed nodes from the front of the queue, and added each undiscovered neighbor to the back. Marking neighbors when enqueued prevented cycles and duplicate queue entries. The function returned the traversal order and safely returned an empty list when the start node was absent from the graph.

The sample adjacency list modeled relationships among six streaming titles. The program printed each node and its neighboring titles, traversed from `City Lights`, then added a direct relationship to `Blue Horizon` and displayed the resulting order. Edge-case demonstrations covered an unknown start node, an empty graph, and a graph containing one isolated node.

BFS runs in O(V + E) time with an adjacency list, where V is the number of reachable vertices and E is the number of examined edges. Its queue and visited set require O(V) additional space in the worst case. For an unweighted graph, BFS discovers nodes in increasing edge distance from the start, making it useful when a recommendation system needs the closest relationship levels first. DFS also runs in O(V + E), but follows a path deeply before backtracking and may use less frontier memory on some graph shapes. DFS does not guarantee the nearest connection first.

## Program Output and Testing

The starter program was run before implementation and displayed the three TODO placeholder messages. After implementation, the program displayed the adjacency list, a level-order traversal, an updated traversal after adding an edge, and results for all three edge cases.

The implementation was checked with deterministic assertions covering expected traversal order, a cycle, a missing start node, an empty graph, a single-node graph, and a neighbor listed without its own adjacency-list key. The program was also run directly with Python 3:

```text
python unit8_discussion.py
```

## Real-World Interpretation

In a streaming recommendation network, BFS can identify content linked directly or through a small number of relationships from a viewer's known preferences. The nearest levels can surface recommendations associated with close connections before less direct matches. DFS can be useful for exploring a chain of related genres or collaborators deeply, such as discovering niche titles through several connections. The choice depends on whether shortest relationship distance or deep path exploration matters more.

## Reflection Essay

The graph traversal exercise strengthened understanding of adjacency lists, queues, visited sets, and cyclic relationships. BFS was implemented by marking each title as discovered when it entered the queue, which prevented repeated scheduling when two titles shared the same neighbor. The most challenging part was preserving true level-by-level order while still avoiding duplicate visits. Tracing the queue after each removal made the discovery order clear and helped verify the implementation.

The streaming catalog example represented titles as nodes and shared genre, cast, or viewer-rating relationships as edges. BFS suited recommendations that prioritized nearby connections, such as titles liked by a viewer's direct network or closely related to a selected program. DFS followed one relationship path deeply before backtracking, making it useful for exploring longer chains or connected components. Both traversals required O(V + E) time with an adjacency list, while their memory use depended on queue or stack behavior and graph shape. BFS offered nearest-level discovery for unweighted graphs; DFS could explore deeply without guaranteeing the shortest connection. Testing missing starts, empty graphs, isolated nodes, and cycles clarified the importance of safe base behavior and visited tracking.

## References

Soyak, T. (2024, July 7). *Depth first search (DFS): A comprehensive guide*. Medium. https://medium.com/@tahsinsoyakk/depth-first-search-dfs-a-comprehensive-guide-89fa4ac94883

Soyak, T. (2024, July 14). *Breadth first search (BFS): A comprehensive guide*. Medium. https://medium.com/@tahsinsoyakk/breadth-first-search-bfs-a-comprehensive-guide-4672bbc5e48c
