'''
Created on Dec 6, 2022

@author: JCSchneider
'''
import NumberTheory
from test.dtracedata import instance


def main():

    print("In main")
    instance = NumberTheory.NumberTheory(9)   
     
    print("Is ", instance.get_the_number(), " even?")
    print(instance.is_even())
    x = 12
    print("Is ", x, " even? ", instance.is_even(x))
          
          
    
    print(instance.get_the_number())
    instance.set_the_number(27)
    print(instance.get_square())
    print("Is prime? " , instance.is_prime())
    
    print("Collatz 27")
    for i in instance.get_collatz():
        print(i, end=" ")
    print()
    print("Collatz 43")
    for i in instance.get_collatz(43):
        print(i, end=" ")
    print()
    
    print("Jugglers 37")
    instance.set_the_number(37)
    for i in instance.get_jugglers():
        print(i, end=" ")
    print()
    print("Jugglers 45")
    for i in instance.get_jugglers(45):
        print(i, end=" ")
    print()
    
    
    print("Prime Factors 3600:")
    instance.set_the_number(3600)    
    for i in instance.get_prime_factors():
        print(i, end=" ")
    print()
    print("Prime Factors 60:")
        
    for i in instance.get_prime_factors(60):
        print(i, end=" ")
    print()
    
    
    print("Factors of 3600")
    for i in instance.get_factors():
        print(i, end=' ')
    print()
    
    print("Factors of 60")
    for i in instance.get_factors(60):
        print(i, end=' ')
    print()
    
    
    print("Reversed 43")
    instance.set_the_number(43)
    print(instance.get_reverse_number())
    
    print("Reciprocal 43")
    print(instance.get_reciprocal_number())
    
    print("To hex 76576500")
    instance.set_the_number(76576500)
    print(instance.get_hex())
    
    print("Is abundant 12")
    instance.set_the_number(12)
    print(instance.is_abundant())
    x = 41
    print(x, " ", instance.is_abundant(x))
    
    print(instance.get_the_number(), " ", instance.get_abundance())
    print(x, " ", instance.get_aliquot_sum(x), " ", instance.get_abundance(x))
    
    print(instance.get_factors_sum(x))
    
    x = 9
    instance.set_the_number(x)
    print("Sigma: " , instance.get_sigma())
    print("Sigma: " , instance.get_sigma(x * 10))
    
    instance.set_the_number(20)
    print("Catalan ", instance.get_catalan())
    print("Catalan ", instance.get_catalan(15))
    
    print("get_fibonacci_list", instance.get_fibonacci_list())
    print("get_fibonacci_list", instance.get_fibonacci_list(15))
    
    
    instance.set_the_number(15)
    print("get_motzin", instance.get_motzkin())
    print("get_motzin", instance.get_motzkin(20))
    
    instance.set_the_number(10)
    print("getPellList: " , instance.get_pell_list())
    print("getPellList: " , instance.get_pell_list(12))
    print("getPell: " , instance.get_pell())
    print("getPell: " , instance.get_pell(12))
    
    instance.set_the_number(15)
    print("getJacobsthalList ", instance.get_jacobsthal_list())
    print("getJacobsthalList ", instance.get_jacobsthal_list(12))
    instance.set_the_number(12)
    print("getJacobsthal ", instance.get_jacobsthal())
    print("getJacobsthal ", instance.get_jacobsthal(15))
    
    instance.set_the_number(21)
    print("alternating Factorial: " , instance.get_alternating_factorial())
    
    

if __name__ == '__main__':
    main()