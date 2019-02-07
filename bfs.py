from state import State
from collections import deque
from helpers import move

def init_struct(initial_state: State):
    return deque([initial_state])

def visit(queue):
    return queue.popleft()

def expand(node: State) -> list:
    global nodes_created
    # Create a list of neighbors generating all possible moves from the current state
    neighbors = [State(move(node.state, move_dir), node, move_dir, node.depth+1, node.cost+1)
        for move_dir in ['left', 'right', 'up', 'down']]
    valid_neighbors = [n for n in neighbors if n.state]
    return valid_neighbors

def add(queue, node: State):
    queue.append(node)
