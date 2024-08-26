def is_robot_lost(coordinate, grid_limit):
    if coordinate < 0 or coordinate > grid_limit:
        return True
    else:
        return False