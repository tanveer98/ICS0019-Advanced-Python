import sys
import importlib
import unittest 
sys.path.append('../..')
q = importlib.import_module("quadratic-equation-mhasan-v3.quadratic")

class SimpleTest(unittest.TestCase): 
  
    # Returns True or False.  
    def setUp(self): 
        pass
  
    def test_a_0_returns_empty_tuple(self):
        res = q.calculate(0,1,5)
        self.assertEqual(res,()) 
        return

    def test_negative_disc_returns_empty_tuple(self):
        res = q.calculate(100,2,3)
        self.assertEqual(res,())

    def test_non_empty_tuple(self):
        res = q.calculate(1,25,5)
        self.assertNotEqual(res,())
        return

    # def startTest(self):
    #     a_0_returns_empty_tuple()
    #     negative_disc_returns_empty_tuple()
    #     non_empty_tuple()
    #     return
    
if __name__ == "__main__":
    unittest.main()