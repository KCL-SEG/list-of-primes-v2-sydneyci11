"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    
    if number_of_primes<1:
        raise ValueError("Numbers cannot be zero or negative.")
    
    list = [] 
    i=2
    
    while len(list) != number_of_primes:
        if isPrimes(i):
            list.append(i)
            i+=1
        else:
            i+=1
                 
    return list
    
def isPrimes(n):
    for k in range(2,n):
        if n%k == 0:
            return False
    else:
            return True
