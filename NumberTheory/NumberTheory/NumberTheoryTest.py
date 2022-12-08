'''
Created on Dec 6, 2022

@author: JCSchneider
'''
import unittest
import NumberTheory


class Test(unittest.TestCase):


    def setUp(self):
        print("In method: ", self._testMethodName , " " , self._testMethodDoc)
        


    def tearDown(self):
        pass

    def testisEven(self):
        instance = NumberTheory.NumberTheory(13)   
        instance.set_the_number(914)     
        self.assertTrue(instance.is_even())        
        #self.assertTrue(instance.is_even(12))
        
     
    def testIsAbundant(self):
        instance = NumberTheory.NumberTheory(12)
        self.assertTrue(instance.is_abundant())
        self.assertTrue(instance.is_abundant(96))
    
     
        
    def testGetNumber(self):
        instance = NumberTheory.NumberTheory(15)                      
        instance.set_the_number(91)
        expected = 91
        result = instance.get_the_number()        
        self.assertEqual(result, expected)
        
        
    def testGetCollatz(self):
        instance = NumberTheory.NumberTheory(5)
        expected = [5, 16, 8, 4, 2, 1]
        result = instance.get_collatz()
        self.assertListEqual(expected, result,"Collatz list should be equal")
        self.assertCountEqual(expected, result, "Collatz count should be equal")
     
    def testGetJugglers(self):   
        instance = NumberTheory.NumberTheory(5)
        expected = [5, 11, 36, 6, 2, 1]
        result = instance.get_jugglers()
        self.assertListEqual(expected, result,"Jugglers list should be equal")
        self.assertCountEqual(expected, result, "Jugglers count should be equal")
        result = instance.get_jugglers(37)
        expected = [37, 225, 3375, 196069, 86818724, 9317, 899319, 852846071, 24906114455136, 4990602, 2233, 105519, 34276462, 5854, 76, 8, 2, 1]
        self.assertListEqual(expected, result,"Jugglers list should be equal")
        self.assertCountEqual(expected, result, "Jugglers count should be equal")
        
    def testGetPrimeFactors(self):
        instance = NumberTheory.NumberTheory(3600)
        expected = [2, 2, 2, 2, 3, 3, 5, 5]
        result = instance.get_prime_factors()
        self.assertListEqual(expected, result,"Prime Factors list should be equal")
        self.assertCountEqual(expected, result, "Prime Factors count should be equal")

    def testGetFactors(self):
        instance = NumberTheory.NumberTheory(3600)
        expected = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 30, 36, 40, 45, 48, 50, 60, 72, 75, 80, 90, 100, 120, 144, 150, 180, 200, 225, 240, 300, 360, 400, 450, 600, 720, 900, 1200, 1800, 3600 ]
        result = instance.get_factors()
        self.assertListEqual(expected, result,"Factors list should be equal")
        self.assertCountEqual(expected, result, "Factors count should be equal")

    def testAliquotSum(self):
        instance = NumberTheory.NumberTheory(60)
        expected = 108
        result = instance.get_aliquot_sum()
        self.assertEquals(result, expected, "Aliquot sum()")
        
    def testGetReverseNumber(self):
        instance = NumberTheory.NumberTheory(34)
        result = instance.get_reverse_number()
        expected = 43
        self.assertEquals(result, expected, "Reversed Number")
        result = instance.get_reverse_number(95)
        expected = 59
        self.assertEquals(result, expected, "Reversed Number")
     
    def testGetReciprocalNumber(self):
        instance = NumberTheory.NumberTheory(43)
        result = instance.get_reciprocal_number()
        expected =  0.023255813953488372
        self.assertAlmostEqual(result, expected, 7, "Reciprocal Number", delta=None)  
        result = instance.get_reciprocal_number(4)
        expected =  0.25
        self.assertAlmostEqual(result, expected, 7, "Reciprocal Number", delta=None)
        
        
    def testGetHex(self):
        instance = NumberTheory.NumberTheory(76576500)
        result = instance.get_hex()
        expected = "49076F4"
        self.assertEquals(result, expected, "Get Hex")
        result = instance.get_hex(84)
        expected = "54"
        self.assertEquals(result, expected, "Get Hex")
    
    def testGetOctal(self):
        instance = NumberTheory.NumberTheory(76576500)
        result = instance.get_octal()
        expected = "444073364"
        self.assertEquals(result, expected, "Get Octal")
        result = instance.get_octal(76576501)
        expected = "444073365"
        self.assertEquals(result, expected, "Get Octal")
        
    
    def testGetBinary(self):  
        instance = NumberTheory.NumberTheory(76576500)
        result = instance.get_binary()
        expected = "100100100000111011011110100"
        self.assertEquals(result, expected, "Get Hex")
        result = instance.get_binary(845)
        expected = "1101001101"
        self.assertEquals(result, expected, "Get Hex")
   
    def testIsPerfect(self):
        instance = NumberTheory.NumberTheory(8128)        
        self.assertTrue(instance.is_perfect())
        self.assertTrue(instance.is_perfect(496))
        self.assertFalse(instance.is_perfect(495))
        
    def testGetSigma(self):
        instance = NumberTheory.NumberTheory(9)
        result = instance.get_sigma()
        expected = 13
        self.assertEquals(result, expected, "Get Sigma")
        result = instance.get_sigma(15)
        expected = 24
        self.assertEquals(result, expected, "Get Sigma")
        
    def testGetKynea(self):
        instance = NumberTheory.NumberTheory(5)
        result = instance.get_kynea()
        expected = 1087
        self.assertEquals(result, expected, "Get Kynea")
        result = instance.get_kynea(6)
        expected = 4223
        self.assertEquals(result, expected, "Get Kynea")
        
    def testGetCarol(self):
        instance = NumberTheory.NumberTheory(7)
        result = instance.get_carol()
        expected = 16127
        self.assertEquals(result, expected, "Get Carol")
        self.assertEquals(65023, instance.get_carol(8), "Get Carol")   
        self.assertNotEquals(615023, instance.get_carol(7), "Get Carol")
        
        
    def testGetFactorials(self):
        instance = NumberTheory.NumberTheory(10)
        result = instance.get_factorials()
        expected = 3628800
        self.assertEquals(result, expected, "Get Factorials")
        result = instance.get_factorials(12)
        expected = 479001600
        self.assertEquals(result,expected,"Get Factorials")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
