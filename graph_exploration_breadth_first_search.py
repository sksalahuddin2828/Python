# Graph Exploration with Breadth-First Search

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

explored = []

def breadth_first_search(explored_nodes, graph, start_node, target_node):
    queue = []
    queue.append(start_node)
    explored_nodes.append(start_node)

    while queue:
        current_node = queue.pop(0)
        if current_node == target_node:
            print("\nHooray! Found the target node:", current_node)
            break

        print(current_node, end=" -> ")

        for neighbor in graph[current_node]:
            if neighbor not in explored_nodes:
                explored_nodes.append(neighbor)
                queue.append(neighbor)

breadth_first_search(explored, graph, 'A', 'G')


# Answer: A -> B -> C -> D -> E -> F -> 
#         Hooray! Found the target node: G

