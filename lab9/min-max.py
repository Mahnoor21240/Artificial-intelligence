# Define a constant for infinity
INFINITY = float('inf')

# Define a simple game tree for demonstration purposes
# The tree is represented as a dictionary where each key is a node,
# and the value is either a list of child nodes (for non-terminal nodes) or a single value (for terminal nodes)
game_tree = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': 3,   # Leaf node with value 3
    'F': 5,   # Leaf node with value 5
    'G': 6,   # Leaf node with value 6
    'H': 9,   # Leaf node with value 9
    'I': 1,   # Leaf node with value 1
    'J': 2    # Leaf node with value 2
}

# Minimax function
def minimax(node, depth, maximizing_player):
    # If we've reached the maximum depth or the node is a terminal node, return its value
    if depth == 0 or is_terminal_node(node):
        return get_node_value(node)

    if maximizing_player:
        max_eval = -INFINITY
        # Iterate through each child of the node
        for child in get_child_nodes(node):
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = INFINITY
        # Iterate through each child of the node
        for child in get_child_nodes(node):
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

# Helper functions
def is_terminal_node(node):
    # A node is terminal if it has no children (i.e., it's a leaf node)
    return node not in game_tree or isinstance(game_tree[node], int)

def get_node_value(node):
    # Return the value of a terminal node
    return game_tree[node]

def get_child_nodes(node):
    # Return the list of child nodes of the current node
    return game_tree[node]

# Example usage
root_node = 'A'  # Start from node A
depth = 3  # Set the maximum depth for the search
result = minimax(root_node, depth, True)
print("The optimal value is:", result)
