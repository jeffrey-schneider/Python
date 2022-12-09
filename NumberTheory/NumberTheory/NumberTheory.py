'''
Created on Dec 6, 2022

@author: JCSchneider
'''
import math
import functools
from fontTools.misc.textTools import num2binary

# def prime_factors(n):
#     i = 2
#     while i*i <=n :
#         if n % 1 == 0:
#             n /= i
#             yield i
#         else:
#             i += 1
#     if n > 1:
#         yield n 


class NumberTheory:    
        
    def __init__(self, theNumber):
        self.__theNumber = theNumber
        
    def set_the_number(self, theNumber):
        self.__theNumber = theNumber
        
    def get_the_number(self):
        return self.__theNumber
    
    def get_square(self, v = None):
        if v == None:
            return self.__theNumber * self.__theNumber
        else:
            return v * v
            
    # https://www.scaler.com/topics/function-overloading-in-python/
    def get_cube(self, v = None):
        if v == None:
            return self.__theNumber * self.__theNumber * self.__theNumber
        else:
            return v * v * v
    
    def is_prime(self, v = None):
        if v == None:
            stopVal = int(math.sqrt(self.get_the_number()))
        else:
            stopVal = int(v)  
        i = 2
        while i <= stopVal:
            if self.__theNumber % i == 0:
                return False
            i+=1
        return True

    def get_collatz(self, v = None):
        retVal = []
        if v == None:
            retVal.append(self.get_the_number())
            counter = self.get_the_number()
        else:
            retVal.append(int (v));
            counter = int(v)
        while counter > 1:
            if counter % 2 == 0:
                counter /= 2;
                counter = int(counter)
            else:
                counter = int(math.floor(3.0*counter+1))
            retVal.append(counter)
        return retVal
    
    def get_jugglers(self, v = None):
        factr = 0.0
        retVal = []
        if v == None:
            retVal.append(self.get_the_number())
            counter = self.get_the_number()
        else:
            retVal.append(v)
            counter = v
        while counter > 1:
            if counter % 2 == 0 :
                factr = .5
            else:
                factr = 1.5
            counter = int(math.floor(math.pow(counter, factr)))
            retVal.append(counter)
        return retVal
    
    
    
    
    def get_prime_factors(self, v = None):
        retVal = []
        if v == None:
            ourNumber = self.get_the_number()
        else:
            ourNumber = v 
        for i in range(2, self.get_the_number()):
            while ourNumber % i == 0:
                retVal.append(i)
                ourNumber /= i
        return retVal
        
               
    def get_factors(self, v=None):
        retVal = []
        if v == None:
            x = self.get_the_number()
        else:
            x = v
        for i in range(1, x+1):
            if x % i == 0:
                retVal.append(i)
        return retVal

    def get_factors_sum(self, v = None):
        retVal = 0
        if v == None:
            for i in self.get_factors():
                retVal += i 
        else:
            for i in self.get_factors(v):
                retVal += i
        return retVal
    
    
    """
    @author: Jeffrey Schneider
    """
    def get_aliquot_sum(self, v=None):
        retVal = 0
        if v == None:
            for i in self.get_factors():
                retVal += i
            return retVal - self.get_the_number()
        else:
            for i in self.get_factors(v):
                retVal += i 
            return retVal - v
       
    
    
    def get_reverse_number(self, v=None):
        rev = 0
        digit = 0
        if v == None:
            num = self.get_the_number()
        else:
            num = v
        
        while num != 0:
            digit = num % 10
            rev = rev * 10 + digit
            num //= 10
        return rev


    def get_reciprocal_number(self, v=None):
        if v == None:
            return 1.0 / self.get_the_number()
        else:
            return 1 / v
    
    
    def get_hex(self, v=None):
        retVal = ""
        hexList = [ "0","1","2","3","4","5","6","7","8", "9", "A", "B", "C", "D","E","F"]
        rem = 0
        if v == None:
            buffer = self.get_the_number()
        else:
            buffer = v
        while buffer > 0:
            rem = buffer % 16
            retVal = hexList[rem] + retVal
            buffer //= 16
            
        return retVal
     
    def get_octal(self, v=None):
        retVal= ""
        dlg  = [ "0", "1","2","3","4","5","6","7"]
        rem = 0
        if v == None:
            buffer = self.get_the_number()
        else:
            buffer = v 
        while buffer > 0:
            rem = buffer % 8
            retVal = dlg[rem] + retVal
            buffer //= 8
        return retVal
            
        
    def get_binary(self, v=None):
        if v == None:
            x = self.get_the_number()
        else:
            x = v        
        #retVal = '{0:b}'.format(self.get_the_number())
        retVal = '{0:b}'.format(x)
        return retVal
        
        
    def is_abundant(self, v=None):
        """Boolean.
        Is the number's aliquot sum greater than the number?
        """
        if v == None:
            return self.get_aliquot_sum()> 0
        else:
            return self.get_aliquot_sum(v) > 0
    
    def get_abundance(self, v=None):
        if v== None:
            return self.get_aliquot_sum() - self.get_the_number()
        else:
            return self.get_aliquot_sum(v) - v    
        
    def is_even(self, v=None):
        if v == None:
            #return self.get_the_number() % 2            
            return self.get_the_number()%2==0        
        else:
            return v % 2 ==0  
        
        
    def is_perfect(self, v= None):
        if v == None:
            return self.get_abundance() == 0
        else:
            return self.get_abundance(v) == 0   
        
   
    def get_kynea(self, v = None):
        if v == None:
            v = self.get_the_number()
            
        kyneaA = math.pow(4.0, v)
        kyneaB = math.pow(2.0, v +1.0)
        kyneaFinal = kyneaA + kyneaB - 1.0
        return int(kyneaFinal)
            
            
    def get_carol(self, v = None):
        if v == None:
            v = self.get_the_number()
        carolA = math.pow(4.0, v )
        carolB = math.pow(2.0, v + 1)
        carolFinal = carolA - carolB - 1.0
        return int(carolFinal)
    
    #@functools.cache
    def get_factorial(self, v = None):
        retVal= 1
        if v == None:
            v = self.get_the_number()
            
        for i in range(1,v +1):
            retVal *= i 
        return retVal
        
         
    def get_sigma(self, v=None):        
        if v == None:
            v = self.get_the_number()            
        if v == 1:
            return 1
        result = 0
        for num in range(1,v+1):
            if v % num == 0:
                result += num
        return result
    
        
    def get_catalan(self, v=None):
        if v == None:
            v = self.get_the_number()        
        catA = self.get_factorial(2*v)
        catB = self.get_factorial(v + 1)
        catC = self.get_factorial(v )
        catFinal = catA / (catB * catC);
        return catFinal
        
     
    def get_fibonacci_list(self, v=None):
        if v == None:
            v = self.get_the_number()
        num1 = 0
        num2 = 1
        counter = 0
        retList = []
        while counter < v:
            retList.append(num1)
            num3 = num2 + num1
            num1 = num2
            num2 = num3
            counter += 1
        return retList
    
    def get_lucas_list(self, v = None):
        retList = []
        if v == None:
            v = self.get_the_number()
        num1 = 2;
        num2 = 1;
        counter = 0
        
        while counter < v:
            retList.append(num1)
            num3 = num2 + num1
            num1 = num2
            num2 = num3
            counter+=1
        return retList
            
            
    def get_motzkin(self, v=None):
        memo = {}
          
        if v == None:
            v = self.get_the_number()
         
        if (v == 0) or ( v == 1):
            return 1
        
        if v in memo:
            return memo.get(v)
        
        m1 = self.get_motzkin(v - 1)
        m2 = self.get_motzkin(v - 2)  
        
        firstPart = (2 * v + 1) * m1
        secondPart = (3 * v - 3) * m2
        lastPart = v + 2
        retVal = (firstPart + secondPart) / lastPart
        memo[v] = retVal
        
        return retVal
     
    
    def get_pell_list(self, v=None):
        if v == None:
            v = self.get_the_number()
        num1 = 0
        num2 = 1
        counter = 0
        retList = []
        while counter < v:
            retList.append(num1)
            num3 = 2 * num2 + num1
            num1 = num2
            num2 = num3
            counter += 1
        return retList
     
    def get_pell(self, v=None):
        theList = []        
        if v == None:
            v = self.get_the_number()
        theList = self.get_pell_list(v)
        theStack = [x for x in theList]
        return theStack.pop()

    
    def get_jacobsthal_list(self, v=None):
        if v == None:
            v = self.get_the_number()
        theList = []
        num1 = 0
        num2 = 1
        counter = 1
        while counter < v:
            theList.append(num1)
            num3 = num2 + 2 * num1
            num1 = num2
            num2 = num3
            counter += 1
        return theList 
    
    def get_jacobsthal(self, v=None):        
        if v == None:
            v = self.get_the_number()
        theList = []
        theList = self.get_jacobsthal_list(v)
        theStack = [x for x in theList]
        return theStack.pop()
    
    
    def get_alternating_factorial(self, v=None):
        if v == None:
            v = self.get_the_number()
        theDictionary = {}
        theDictionary[1] = 1
        theDictionary[2] = 1
        for i in range(3,v+1):
            theDictionary[i] = self.get_factorial(i) - theDictionary[i-1]
        return theDictionary.get(v)
        