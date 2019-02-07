#!/usr/local/bin/python3
# coding=utf-8

import timeit
from state import State
from collections import deque
from argparse import ArgumentParser
from drivers import methods
from helpers import read_board_input, read_file_input, target_state

seen = set()

# for result output
goal_node: State = None
nodes_visited = 0
nodes_created = 0

# def expand(node: State) -> list:
#     global nodes_created
#     # Create a list of neighbors generating all possible moves from the current state
#     neighbors = [State(move(node.state, move_dir), node, move_dir, node.depth+1, node.cost+1)
#         for move_dir in ['left', 'right', 'up', 'down']]
#     nodes_created += 4
#     return [n for n in neighbors if n.state]

def solve(initial_state, method_name):
    global seen, goal_node, nodes_visited, nodes_created
    init_struct, visit, expand, add = methods[method_name]

    # keep track of which nodes we have visited and which we have to visit 
    struct = init_struct(State(initial_state))
    nodes_created += 1
    while struct:
        node = visit(struct)
        seen.add(node)

        nodes_visited += 1
        if node.state == target_state:
            # mark the node that contains the solution
            goal_node = node
            return struct

        neighbors = expand(node)
        nodes_created += len(neighbors)

        for neighbor in neighbors:
            if neighbor not in seen:
                add(struct, neighbor)
                seen.add(neighbor)

def get_path():
    curr = goal_node
    path = [goal_node.move]
    while curr.parent:
        curr = curr.parent
        path.insert(0, curr.move)
    return path[1:]

def output(time):
    if not goal_node:
        print('Solution not found')
    else:
        print('Cost of path:', goal_node.depth)
        print('Path to goal:', ', '.join(get_path()))
    print('# visited nodes:', nodes_visited)
    print('Running time (secconds):', format(time, '.8f'))
    print('Used memory:', 'If each node requires only 72 bytes, {}'.format(nodes_created * 72))

def main():
    parser = ArgumentParser()
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument('-f', '--file', help='set input file path')
    input_group.add_argument('-b', '--board', help='set board input text')
    parser.add_argument('-s', '--separator', help='set separator for each element of board input')
    parser.add_argument('-m', '--method', help="'bfs' or 'a_star'")
    parser.set_defaults(separator=' ', method='bfs')
    input_group.set_defaults(file='board.txt')
    args = parser.parse_args()
    initial_state = []
    if args.board:
        initial_state = read_board_input(args.board, args.separator)
    else:
        initial_state = read_file_input(args.file, args.separator)
    start = timeit.default_timer()
    solve(initial_state, args.method)
    stop = timeit.default_timer()
    output(stop-start)

if __name__ == "__main__":
    main()
