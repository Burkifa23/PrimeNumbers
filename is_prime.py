import math

def is_prime(n):
    """
    Checks if a given number n is prime, using the square root and 6k +/- 1 optimizations.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True # 2 and 3 are prime
    
    # 1. Check for divisibility by 2 and 3
    if n % 2 == 0 or n % 3 == 0:
        return False
        
    # 2. Check for factors up to the square root of n
    # Start checking from 5 and increment by 6
    i = 5
    while i * i <= n:
        # Check for i (6k - 1) and i + 2 (6k + 1)
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True
