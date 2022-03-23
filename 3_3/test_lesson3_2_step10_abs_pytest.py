class TestAbsPytest:
    def test_abs1(self):
        assert abs(-42) == 42, "Should be absolute value of a number"

    def test_abs2(self):
        assert abs(-42) == -42, "Should be absolute value of a number"
