from position_calculator import position_calculator

class TestIntegration():

    def test_integration_one(self):
        input = ['4 8', '(2, 3, E) LFRFF', '(0, 2, N) FFLFRFF']
        output = ['(4, 4, E)', '(0, 4, W) LOST']
        assert position_calculator(input) == output

    def test_integration_two(self):
        input = ['4 8', '(2, 3, N) FLLFR', '(1, 0, S) FFRLF']
        output = ['(2, 3, W)', '(1, 0, S) LOST']
        assert position_calculator(input) == output