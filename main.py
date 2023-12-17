import random

# Determine prime number
def isPrime(num):
    # The number is not prime if smaller than 2 or not integer
    if num < 2 or type(num) is not int:
        return False

    # Check if divisible
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

# Generate random prime number
def generatePrime(min, max):
    primes = [i for i in range(min, max) if isPrime(i)]
    n = random.choice(primes)
    return n

# Find coprime number; 2<e<pi(n), gcd(e, pi(n)) == 1  ;;

