class State:
    def __init__(self, state: list, parent=None, move: str=None, depth=0, cost=0, key=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.key = key
        if self.state:
            self.id = ''.join(str(e) for e in self.state)

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.cost < other.cost

    def __hash__(self):
        return int(self.id)

    def __repr__(self):
        return str(self.state)
