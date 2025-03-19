
import unittest
from phase1 import SList2

class Test(unittest.TestCase):


   	#setUp is a method which is ran before a test method is executed. 
   	#This is useful if you need some data (for example) to be present before running a test.
    def setUp(self):
	



        # -------- Exercise 3 ---------------
        l = SList2()

        for _ in range(7):
            l.addLast(_)

        print("Original list: ", l)
        l.leftrightShift(False, 2)
        print("List after performing a right shift:", l)
        # do another shift (left) to show the original list again
        l.leftrightShift(True, 2)
        print(l)

	
    
    
    
    
    
    
    
    #implement here your test cases

















        
if __name__ == "__main__":
    unittest.main()