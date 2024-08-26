from direction_utilities import is_robot_lost
class Robot:
    direction_list = ["N", "E", "S", "W"]
    length_of_list = len(direction_list)

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
        current_direction_index = self.direction_list.index(self.direction.strip(' '))
        if(not self._lost):
            if(current_direction_index >= 1):
                self._direction = self.direction_list[(current_direction_index-1)]
            else:
                self._direction = self.direction_list[(self.length_of_list-1)]

    def turn_right(self):
        current_direction_index = self.direction_list.index(self.direction.strip(' '))
        if(not self._lost):
            if(current_direction_index <= (self.length_of_list-2)):
                self._direction = self.direction_list[(current_direction_index+1)]
            else:
                self._direction = self.direction_list[0]

    def move_forward(self):
        if not self._lost:
            if self._direction == "N":
                new_y = self._y + 1
                new_x = self.x
            elif self._direction == "E":
                new_x = self._x + 1
                new_y = self._y
            elif self._direction == "S":
                new_y = self._y - 1
                new_x = self._x
            elif self.direction == "W":
                new_x = self._x - 1
                new_y = self._y

            if is_robot_lost(new_x, self._grid_x) or is_robot_lost(new_y, self._grid_y):
                self._lost = True
            else:
                self._y = new_y
                self._x = new_x


    def print_status(self):
        if self._lost:
            return f"({self._x}, {self._y}, {self._direction}) LOST"
        else:
            return f"({self._x}, {self._y}, {self._direction})"


