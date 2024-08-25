import pytest
from unittest.mock import Mock, call
from robot import Robot
from position_calculator import grid_x, grid_y, process_grid_line, process_robot_line, process_robot_details, process_robot_actions

class TestPositionCalculator:

    @pytest.fixture
    def robot():
        return Robot(2,3,'E',4,8)

    def test_process_grid_line():
            process_grid_line('4 8')
            assert grid_x == 4
            assert grid_y == 8

    # def test_process_robot_line():
    #         assert process_robot_line('(2, 3, E) LFRFF')

    def test_process_robot_details():
            robot = process_robot_details('2,3,E')
            assert robot.x == 2
            assert robot.y == 3
            assert robot.direction == 'E'
            assert robot.lost == False

    def test_process_robot_actions(robot):
            robot_mock = Mock()
            process_robot_actions(robot_mock, 'LFRFF')
            expected_calls = [call.turn_left(), call.move_forward(), call.turn_right(), call.move_forward(), call.move_forward()]
            robot_mock.assert_has_calls(expected_calls, any_order = False)

