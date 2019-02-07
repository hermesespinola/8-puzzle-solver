board_len, board_side = 9, 3

def read_board_input(conf: str, separator: str) -> list:
    initial_state = [int(x) for x in conf.split(separator)]
    if board_len != len(initial_state):
        'board must be 9 comma separated numbers'
    return initial_state

def read_file_input(path: str, separator: str) -> list:
    with open(path, 'r') as board_file:
        lines = board_file.read().splitlines()
        return read_board_input(separator.join(lines), separator)

def swap(lst: list, i1, i2) -> list:
    tmp = lst[i1]
    lst[i1] = lst[i2]
    lst[i2] = tmp
    return lst

def move(state: list, direction: str) -> list:
    # 0 represents the empty spot
    _state = state[:]
    empty_space = _state.index(0)
    if direction == 'up':
        if empty_space not in range(0, board_side):
            return swap(_state, empty_space - board_side, empty_space)
        else:
            return None
    if direction == 'down':
        if empty_space not in range(board_len - board_side, board_len):
            return swap(_state, empty_space + board_side, empty_space)
        else:
            return None
    if direction == 'left':
        if empty_space not in range(0, board_len, board_side):
            return swap(_state, empty_space - 1, empty_space)
        else:
            return None
    if direction == 'right':
        if empty_space not in range(board_side - 1, board_len, board_side):
            return swap(_state, empty_space + 1, empty_space)
        else:
            return None
