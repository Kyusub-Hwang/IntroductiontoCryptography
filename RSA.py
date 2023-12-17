import random
import math
import time

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

# Generate public key; 2<e<pi(n), gcd(e, phi(n)) == 1
def generatepublicKey(phi):
    # Condition 1) 2<e<pi(n)
    e = random.randint(3, phi-1)
    # Condition 2) gcd(e, phi(n)) == 1
    while math.gcd(e, phi) != 1:
        e = random.randint(3, phi-1)
    return e

def generatePrivateKey(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("Failed to generate private key")

if __name__ == '__main__':
    # Generate p,q; p !== q
    p, q = generatePrime(100, 200), generatePrime(200, 300)

    n = p * q
    phi = (p-1) * (q-1)

    publicKey = generatepublicKey(phi)
    privateKey = generatePrivateKey(publicKey, phi)

    print(f'p: {p}')
    print(f'q: {q}')
    print(f'n: {n}')
    print(f'phi of n: {phi}')
    print(f'public Key: {publicKey}')
    print(f'private Key: {privateKey}')

    message = "Hello World"
    print(f'message: {message}')
    # Message Encoding; (m ^ e) mod n = c
    messageEncoded = [ord(ch) for ch in message]
    ciphertext = [pow(ch, publicKey, n) for ch in messageEncoded]
    print(f'ciphertext: {ciphertext}')

    messageDecoded = [pow(ch, privateKey, n) for ch in ciphertext]
    message = "".join(chr(ch) for ch in messageDecoded)
    print(f'message: {message}')









