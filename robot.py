from direction_utilities import is_robot_lost
class Robot:

    def __init__(self, x, y, direction, grid_x, grid_y):
        self._x = x
        self._y = y
        self._direction = direction.strip()
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
        direction_list = ["N", "E", "S", "W"]
        length_of_list = len(direction_list)
        current_direction_index = direction_list.index(self.direction.strip(' '))
        if(not self._lost):
            if(current_direction_index >= 1):
                self._direction = direction_list[(current_direction_index-1)]
            else:
                self._direction = direction_list[(length_of_list-1)]

    def turn_right(self):
        direction_list = ["N", "E", "S", "W"]
        length_of_list = len(direction_list)
        current_direction_index = direction_list.index(self.direction)
        if(not self._lost):
            if(current_direction_index <= (length_of_list-2)):
                self._direction = direction_list[(current_direction_index+1)]
            else:
                self._direction = direction_list[0]

    def move_forward(self):
        if not self._lost:
            if self._direction == "N":
                new_y = self._y + 1
                if is_robot_lost(new_y, self._grid_y):
                    self._lost = True
                else:
                    self._y = new_y
            if self._direction == "E":
                new_x = self._x + 1
                if is_robot_lost(new_x, self._grid_x):
                    self._lost = True
                else:
                    self._x = new_x
            if self._direction == "S":
                new_y = self._y - 1
                if is_robot_lost(new_y, self._grid_y):
                    self._lost = True
                else:
                    self._y = new_y
            if self.direction == "W":
                new_x = self._x - 1
                if is_robot_lost(new_x, self._grid_x):
                    self._lost = True
                else:
                    self._x = new_x

    def print_status(self):
        if self._lost:
            return f"({self._x}, {self._y}, {self._direction}) LOST"
        else:
            return f"({self._x}, {self._y}, {self._direction})"


