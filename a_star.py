from state import State
import heapq
from helpers import move, target_state, board_side, memoize

find_target_index = memoize(target_state.index)

def calc_cost(board_conf: list, depth):
    total_cost = 0
    for idx, piece in enumerate(board_conf):
        if piece == 0:
            continue
        target_idx = find_target_index(piece)
        v_cost = abs(idx // board_side - target_idx // board_side)
        h_cost = abs((idx % board_side) - (target_idx % board_side))
        total_cost += v_cost + h_cost
    return total_cost + depth

def init_struct(initial_state: State):
    h = [initial_state]
    heapq.heapify(h)
    return h

def visit(heap):
    return heapq.heappop(heap)

def expand(node: State) -> list:
    neighbors = []
    for move_dir in ['left', 'right', 'up', 'down']:
        board_conf = move(node.state, move_dir)
        if not board_conf:
            continue
        cost = calc_cost(board_conf, node.depth+1)
        # Create a list of neighbors generating all possible moves from the current state
        neighbors.append(State(board_conf, node, move_dir, node.depth+1, cost))
    return neighbors

def add(heap, node: State):
    heapq.heappush(heap, node)
