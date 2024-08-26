import pytest
from unittest.mock import Mock, call
from robot import Robot
from position_calculator import process_grid_line, process_robot_line, process_robot_details, process_robot_actions

class TestPositionCalculator:

    def test_process_grid_line(self):
        x,y = process_grid_line('4 8')
        assert x == 4
        assert y == 8

    def test_process_robot_line(self):
        robot = process_robot_line('(2, 3, N) FLLFR', 4, 8)
        assert robot.x == 2
        assert robot.y == 3
        assert robot.direction == 'W'

    def test_process_robot_details(self):
        robot = process_robot_details('2,3,E',4,4)
        assert robot.x == 2
        assert robot.y == 3
        assert robot.direction == 'E'
        assert robot.lost == False

    def test_process_robot_actions(self):
        robot_mock = Mock()
        robot_mock.return_value = False
        process_robot_actions(robot_mock, 'LFRFF')
        expected_calls = [call.turn_left(), call.move_forward(), call.turn_right(), call.move_forward(), call.move_forward()]
        robot_mock.assert_has_calls(expected_calls, any_order = False)

