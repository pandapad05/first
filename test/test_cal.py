import unittest
import sys
sys.path.append("../src")

import cal

class MysumTest(unittest.TestCase):
    def test_1_sum(self):
        result = cal.sum(10,20)
        assert( result == 30) , "Sum is not correct"

    def test_2_mul(self):
        result = cal.mul(3,3)
        assert (result ==9),"Mul  is not coorect"

    def test3_sub(self):
        assert (cal.sub(10,5) == 5), "Sub is failed"

#    def test9_wrong(self):
#        assert(cal.sum(10,10) == 30),"SUM is wrong"

if __name__ == '__main__':
    unittest.main()


