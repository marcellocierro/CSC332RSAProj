import math as math
import random

def factors(n):
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(e, phi):
    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % phi

def rsa(p, q):
    n = p * q

    g = factors(n)
    print g

    phi = (p-1) * (q-1)

    print "phi(n) = ", phi

    e = random.randrange(1,phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = modinv(e, phi)

    print "Public key = (", e,n, ")"
    print "Private key = (", d,n, ")"
    print "-----------------------------"

def main():
    p = int(raw_input("Enter a prime number: "))
    q = int(raw_input("Enter a different prime number: "))
    print "-----------------------------"
    rsa(p,q)

if __name__ == "__main__":
    main()
