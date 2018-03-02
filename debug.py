import logging
import pdb
import unittest

# try except finally 错误调试
def main0():
    def foo(s):
        n = int(s)
        if n == 0:
            raise ValueError('invalid value: %s' % s)
        return n

    try:
        print('try...')
        r = 10 / foo('56')
        print('result: ', r)
    except ValueError as e:
        print('ValueError: ', e)
    except ZeroDivisionError as e:
        logging.exception(e)
    else:
        print('no error!')
    finally:
        print('finally...')
    print('END')


# 调试方法，1 print(), 2 assert, 3 logging, 4 pdb, 5 IDE
def main1():
    def char2int(s):
        n = int(s)
        pdb.set_trace()
        print('>>> n = %d' % n)
        assert n != 0, 'n is Zero!'
        logging.basicConfig(level=logging.INFO)
        logging.info('n = %d' % n)
        return 10 / n

    print(char2int('9'))

# 单元测试
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score > 100 or self.score < 0:
            raise ValueError('score greater than 100 or less than 0')
        elif self.score >= 80:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

class TestStudent(unittest.TestCase):
    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()


if __name__ == '__main__':
    unittest.main()













    #

