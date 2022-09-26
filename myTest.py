import unittest

class TestingSum(unittest.TestCase):

 def test1(self):
    self.assertEqual(sum([2,3,5]),10,"It should be 10")
    
 def test2(self):
    self.assertEqual(sum([1,3,5]),9,"It should be 10")
    
if __name__=='__main__':
    unittest.main()    






"""def test1():
    assert sum([2,3,5])==10

def test2():
    assert sum([1,4,3])==8
    
if __name__=="__main__"   :
    test1()
    test2()
    print("Everything is correct")  """   