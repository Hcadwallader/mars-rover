from robot import Robot

def position_calculator(input_list):

    output_list = []
    grid_x, grid_y = process_grid_line(input_list[0])
    input_list.pop(0)

    for item in input_list:
        robot = process_robot_line(item, grid_x, grid_y)
        output_list.append(robot.print_status())

    return output_list

def process_grid_line(grid_line):
    grid_ouput = grid_line.split(" ")
    return int(grid_ouput[0]), int(grid_ouput[1])

def process_robot_line(robot_line, grid_x, grid_y):
    robot_details, robot_actions = robot_line.split(")")
    formatted_robot_details = robot_details.strip("(")
    robot = process_robot_details(formatted_robot_details, grid_x, grid_y)
    process_robot_actions(robot, robot_actions)
    return robot

def process_robot_details(robot_details, grid_x, grid_y):
    properties = robot_details.split(',')
    return Robot(int(properties[0]), int(properties[1]), properties[2], grid_x, grid_y)

def process_robot_actions(robot, robot_actions):
    action_list = list(robot_actions)
    for action in action_list:
        if action == 'L':
            robot.turn_left()
        elif action == 'R':
            robot.turn_right()
        elif action == 'F':
            robot.move_forward()
    return robot