INFINITY = float('inf')

# Define the game tree as a dictionary
game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': 3,   # Leaf node with value 3
    'E': 5,   # Leaf node with value 5
    'F': 6,   # Leaf node with value 6
    'G': 9    # Leaf node with value 9
}

# Minimax function with Alpha-Beta pruning
def minimax(node, depth, is_maximizing_player, alpha, beta):
    if is_leaf_node(node):
        return get_node_value(node)

    if is_maximizing_player:
        best_value = -INFINITY

        # Iterate through all child nodes
        for child in get_child_nodes(node):
            value = minimax(child, depth + 1, False, alpha, beta)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)

            # Alpha-Beta pruning
            if beta <= alpha:
                break  # Cutoff

        return best_value
    else:
        best_value = INFINITY

        # Iterate through all child nodes
        for child in get_child_nodes(node):
            value = minimax(child, depth + 1, True, alpha, beta)
            best_value = min(best_value, value)
            beta = min(beta, best_value)

            # Alpha-Beta pruning
            if beta <= alpha:
                break  # Cutoff

        return best_value

# Helper functions
def is_leaf_node(node):
    # A node is a leaf node if it's not in the game tree (i.e., it has no children)
    return not isinstance(game_tree.get(node), list)

def get_node_value(node):
    # Return the value of a leaf node
    return game_tree[node]

def get_child_nodes(node):
    # Return the list of child nodes
    return game_tree[node]

# Example usage
root_node = 'A'  # Start from node A
result = minimax(root_node, 0, True, -INFINITY, INFINITY)
print("The optimal value is:", result)
