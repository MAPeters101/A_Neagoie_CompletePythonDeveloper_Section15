import unittest
import lesson198


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = lesson198.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'shkshks'
        result = lesson198.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))

unittest.main()

