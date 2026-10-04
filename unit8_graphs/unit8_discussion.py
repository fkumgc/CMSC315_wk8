"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # A queue processes the oldest discovered node first, so every node at
    # the current distance is visited before nodes at a greater distance.
    if start not in graph:
        return []

    queue = deque([start])
    visited = {start}  # Mark when enqueued so cycles cannot add duplicates.
    traversal_order = []

    while queue:
        current = queue.popleft()
        traversal_order.append(current)

        # Newly discovered neighbors wait in the queue for their turn. This
        # level-by-level order differs from DFS, which follows one path deeply.
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    # Each node represents a title in a streaming catalog. An edge means two
    # titles share a genre, cast member, or strong viewer-rating relationship.
    graph = {
        "City Lights": ["Midnight Run", "Quiet Harbor"],
        "Midnight Run": ["City Lights", "Neon Streets", "Last Train"],
        "Quiet Harbor": ["City Lights", "Blue Horizon"],
        "Neon Streets": ["Midnight Run", "Last Train"],
        "Last Train": ["Midnight Run", "Neon Streets", "Blue Horizon"],
        "Blue Horizon": ["Quiet Harbor", "Last Train"],
    }

    print("\n=== GRAPH STRUCTURE ===")
    for title, related_titles in graph.items():
        print(f"{title}: {related_titles}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    start_title = "City Lights"
    print("\n=== BFS TRAVERSAL ===")
    print(f"Starting at {start_title}, BFS visits nearby titles level by level:")
    print(" -> ".join(bfs(graph, start_title)))

    # Adding an edge demonstrates that the graph can be updated and traversed
    # again; the new direct connection is discovered before deeper neighbors.
    graph["City Lights"].append("Blue Horizon")
    graph["Blue Horizon"].append("City Lights")
    print("After adding a direct City Lights / Blue Horizon connection:")
    print(" -> ".join(bfs(graph, start_title)))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("Missing start node returns an empty traversal:", bfs(graph, "Unknown Title"))
    print("Empty graph returns an empty traversal:", bfs({}, "City Lights"))
    print("Single-node graph visits its only node:", bfs({"Solo": []}, "Solo"))



if __name__ == "__main__":
    main()
