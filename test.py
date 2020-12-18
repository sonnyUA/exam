import unittest
from exam import Progression


class TestProgression(unittest.TestCase):
    test = Progression(20)
    test2 = Progression(75)
    test3 = Progression(3)
    test4 = Progression(40)
    test_error = Progression(-1)



    def test_summa(self):
        self.assertRaises(ValueError,self.test_error.summa)
        self.assertEqual(self.test.summa(), 1010)
        self.assertTrue(self.test.summa(), isinstance(self.test.summa(), int))
        self.assertEqual(self.test2.summa(), 14100)
        self.assertEqual(self.test3.summa(), 24)
        self.assertEqual(self.test4.summa(), 4020)

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
