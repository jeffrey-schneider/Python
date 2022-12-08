'''
Created on Dec 6, 2022

@author: JCSchneider
'''
import NumberTheory


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
    
    

if __name__ == '__main__':
    main()