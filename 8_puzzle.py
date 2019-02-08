#!/usr/local/bin/python3
# coding=utf-8

import timeit
from pprint import pprint
from state import State
from argparse import ArgumentParser
from drivers import methods
from helpers import read_board_input, read_file_input, target_state

# for result output
nodes_visited = 0
nodes_created = 0
debug = False

def solve(initial_state, method_name):
    global nodes_visited, nodes_created
    goal_node: State = None
    seen = set()
    init_struct, visit, expand, add = methods[method_name]

    # keep track of which nodes we have visited and which we have to visit 
    struct = init_struct(State(initial_state))
    nodes_created += 1
    level = 0
    while struct:
        if debug:
            print('level', level)
            pprint(struct)
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
        level += 1
    return goal_node

def get_path(goal_node: State) -> list:
    curr = goal_node
    path = [goal_node.move]
    while curr.parent:
        curr = curr.parent
        path.insert(0, curr.move)
    return path[1:]

def output(goal_node: State, time: float):
    if not goal_node:
        print('Solution not found')
    else:
        print('Cost of path:', goal_node.depth)
        print('Path to goal:', ', '.join(get_path(goal_node)))
    print('# visited nodes:', nodes_visited)
    print('Running time (seconds):', format(time, '.8f'))
    print('Used memory:', 'If each node requires only 72 bytes, {}'.format(nodes_created * 72))

def main():
    global debug
    parser = ArgumentParser()
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument('-f', '--file', help='set input file path')
    input_group.add_argument('-b', '--board', help='set board input text')
    parser.add_argument('-s', '--separator', help='set separator for each element of board input')
    parser.add_argument('-m', '--method', help="'bfs', 'dfs', or 'a_star'")
    parser.add_argument('-d', '--debug', help='enable debugging logs', action='store_true')
    parser.set_defaults(separator=' ', method='a_star')
    input_group.set_defaults(file='board.txt')
    args = parser.parse_args()
    debug = args.debug
    initial_state = []
    if args.board:
        initial_state = read_board_input(args.board, args.separator)
    else:
        initial_state = read_file_input(args.file, args.separator)
    start = timeit.default_timer()
    goal_node = solve(initial_state, args.method)
    stop = timeit.default_timer()
    output(goal_node, stop-start)

if __name__ == "__main__":
    main()
