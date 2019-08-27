import unittest

from src import mysum

class MysumTest(unittest.TestCase):
    def test_1(self):
        result=mysum(10)
        print ("Result of mysum is",result)


if __name__ == '__main__':
    unittest.main()


