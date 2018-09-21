from ireton import use_session_fixture, define_session_fixture
import unittest

times_expensive_resource_has_been_acquired = 0


@define_session_fixture()
def expensive_resource():
    global times_expensive_resource_has_been_acquired
    times_expensive_resource_has_been_acquired += 1
    return 'the_resource'


@define_session_fixture()
def another_expensive_resource():
    return 'another_resource'


class TestFixture(unittest.TestCase):
    def test_fixture_is_acquired_only_once(self):
        @use_session_fixture()
        def run_test_first(expensive_resource):
            assert expensive_resource == 'the_resource'

        @use_session_fixture()
        def run_test_second(expensive_resource):
            assert expensive_resource == 'the_resource'

        @use_session_fixture()
        def run_test_third(expensive_resource):
            assert expensive_resource == 'the_resource'

        self.assertEqual(times_expensive_resource_has_been_acquired, 1)

    def test_multiple_fixtures_can_be_user(self):
        @use_session_fixture()
        def run_test(expensive_resource, another_expensive_resource):
            self.assertEqual(expensive_resource, 'the_resource')
            self.assertEqual(another_expensive_resource, 'another_resource')
