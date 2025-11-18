def is_prime(n):
    """
    Checks if a given natural number n > 1 is a prime number.
    Returns True if prime, False otherwise.
    """
    # 1 is not considered prime.
    if n <= 1:
        return False
    
    # 2 and 3 are prime.
    if n <= 3:
        return True
    
    # Initial check for divisibility by 2 and 3
    # This loop is the simplest, most direct implementation.
    for i in range(2, n):
        if n % i == 0:
            return False
            
    return True

# Example Usage:
print(is_prime(5))  # True
print(is_prime(6))  # False
print(is_prime(13)) # True
print(is_prime(1))  # False