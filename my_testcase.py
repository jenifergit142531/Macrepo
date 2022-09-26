import unittest
from my_logic import sum

class check(unittest.TestCase):
    def test_all(self):
        
        data=(1,2,3,4)
        result=sum(data)
        self.assertEqual(result, 6)
        
if __name__=='__main__':
    unittest.main()
        