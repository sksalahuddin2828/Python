# Sample data representing hierarchies and edges
hierarchies = {
    1: {('A', 'B'), ('C', 'D'), ('E', 'F')},
    2: {('G', 'H'), ('I', 'J'), ('K', 'L')},
    3: {('M', 'N'), ('O', 'P'), ('Q', 'R')},
}

# A list to represent the order of hierarchies based on hierarchy level
hierarchy_order = [1, 2, 3]

def process_edges(hierarchies, hierarchy_order):
    processed_edges = set()

    # Iterate through the hierarchies based on the hierarchy order
    for h in hierarchy_order:
        edges = hierarchies[h]

        # Check if all edges in the current hierarchy have been processed
        if edges.issubset(processed_edges):
            continue

        # Process the edges in the current hierarchy
        for edge in edges:
            # Your processing logic goes here.
            # For this example, we'll just print the edges.
            print("Processing edge:", edge)

        # Add the processed edges to the set
        processed_edges.update(edges)

# Call the function to process the edges
process_edges(hierarchies, hierarchy_order)



# Answer: Processing edge: ('E', 'F')
#         Processing edge: ('A', 'B')
#         Processing edge: ('C', 'D')
#         Processing edge: ('K', 'L')
#         Processing edge: ('I', 'J')
#         Processing edge: ('G', 'H')
#         Processing edge: ('O', 'P')
#         Processing edge: ('Q', 'R')
#         Processing edge: ('M', 'N')
