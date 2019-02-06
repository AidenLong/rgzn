import unittest


class MyDict(dict):
    pass


class TestMyDict(unittest.TestCase):
    def setUp(self):
        print('测试前准备')

    def tearDown(self):
        print('测试后清理')

    def test_init(self):
        md = MyDict(one=1, two=2)
        self.assertEqual(md['one'], 1)
        self.assertEqual(md['weo'], 2)

    def test_nothing(self):
        pass


if __name__ == '__main__':
    unittest.main()
