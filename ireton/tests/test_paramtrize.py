from ireton import parametrize
import unittest


class TestParametrize(unittest.TestCase):
    def test_parametrized_test(self):
        @parametrize([
            (1, 2),
            (2, 3),
            (3, 4),
        ])
        def run_test(x, y):
            assert x + 1 == y

    def test_failures(self ):
        try:
            @parametrize([
                (1, 1),
                (2, 2),
                (2, 3)
            ])
            def run_test(x, y):
                assert x + 1 == y
        except AssertionError as e:
            assert 'Failed on: (1, 1)' in e.args[0]
            assert 'Failed on: (2, 2)' in e.args[0]
            assert 'Failed on: (2, 3)' not in e.args[0]
