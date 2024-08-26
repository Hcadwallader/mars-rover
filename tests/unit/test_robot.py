from robot import Robot

class TestRobot():

    def test_turn_right_facing_north_end_facing_east(self):
        r = Robot(0,0,'N',2,2)
        r.turn_right()
        assert r.direction == 'E'

    def test_turn_right_facing_east_end_facing_south(self):
        r = Robot(0,0,'E',2,2)
        r.turn_right()
        assert r.direction == 'S'

    def test_turn_right_facing_south_end_facing_west(self):
        r = Robot(0,0,'S',2,2)
        r.turn_right()
        assert r.direction == 'W'

    def test_turn_right_facing_west_end_facing_north(self):
        r = Robot(0,0,'W',2,2)
        r.turn_right()
        assert r.direction == 'N'

    def test_turn_left_facing_north_end_facing_west(self):
        r = Robot(0,0,'N',2,2)
        r.turn_left()
        assert r.direction == 'W'

    def test_turn_left_facing_east_end_facing_north(self):
        r = Robot(0,0,'E',2,2)
        r.turn_left()
        assert r.direction == 'N'

    def test_turn_left_facing_south_end_facing_east(self):
        r = Robot(0,0,'S',2,2)
        r.turn_left()
        assert r.direction == 'E'

    def test_turn_left_facing_west_end_facing_south(self):
        r = Robot(0,0,'W',2,2)
        r.turn_left()
        assert r.direction == 'S'

    def test_move_forward_facing_east_increases_x(self):
        r = Robot(0,0,'E',2,2)
        r.move_forward()
        assert r.x == 1
        assert r.y == 0
        assert r.direction == 'E'

    def test_move_forward_facing_west_decreases_x(self):
        r = Robot(2,2,'W',2,2)
        r.move_forward()
        assert r.x == 1
        assert r.y == 2
        assert r.direction == 'W'

    def test_move_forward_facing_north_increases_y(self):
        r = Robot(2,2,'N',3,3)
        r.move_forward()
        assert r.x == 2
        assert r.y == 3
        assert r.direction == 'N'

    def test_move_forward_facing_south_decreases_y(self):
        r = Robot(1,1,'S',2,2)
        r.move_forward()
        assert r.x == 1
        assert r.y == 0
        assert r.direction == 'S'

    def test_move_forward_facing_east_gets_lost(self):
        r = Robot(2,2,'E',2,2)
        r.move_forward()
        assert r.x == 2
        assert r.y == 2
        assert r.direction == 'E'
        assert r.lost == True

    def test_move_forward_facing_west_gets_lost(self):
        r = Robot(0,0,'W',1,1)
        r.move_forward()
        assert r.x == 0
        assert r.y == 0
        assert r.direction == 'W'
        assert r.lost == True

    def test_move_forward_facing_north_gets_lost(self):
        r = Robot(2,2,'N',2,2)
        r.move_forward()
        assert r.x == 2
        assert r.y == 2
        assert r.direction == 'N'
        assert r.lost == True

    def test_move_forward_facing_south_gets_lost(self):
        r = Robot(0,0,'S',3,3)
        r.move_forward()
        assert r.x == 0
        assert r.y == 0
        assert r.direction == 'S'
        assert r.lost == True

    def test_print_status(self):
        r = Robot(4,4,'E',2,2)
        assert r.print_status() == '(4, 4, E)'

    def test_print_status_robot_lost(self):
           r = Robot(2,2,'N',2,2)
           r.move_forward()
           assert r.print_status() == '(2, 2, N) LOST'

