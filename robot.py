class Robot:

    def __init__(self, x, y, direction, grid_x, grid_y):
        self._x = x
        self._y = y
        self._direction = direction
        self._grid_x = grid_x
        self._grid_y = grid_y
        self._lost = False

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def direction(self):
        return self._direction

    @property
    def lost(self):
        return self._lost

    @property
    def grid_x(self):
        return self._grid_x

    @property
    def grid_y(self):
        return self._grid_y

    def turn_left(self):
        raise NotImplementedError("turn_left")

    def turn_right(self):
        raise NotImplementedError("turn_right")

    def move_forward(self):
        raise NotImplementedError("move_forward")

    def print_status(self):
        raise NotImplementedError("move_forward")

