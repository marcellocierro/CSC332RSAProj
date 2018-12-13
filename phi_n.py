import math as math
import random

#Testing a simple factorization method
def factors(n):
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

#Euclidean to determine greatest common divsor
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
    #Compute n
    n = p * q

    g = factors(n)

    #Commpute phi
    phi = (p-1) * (q-1)

    #Choose encrypted exponenet, e
    e = random.randrange(1,phi)

    #use Eucldiean to verify e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # compute d
    d = modinv(e, phi)

    return ((e, n), (d, n))

def encrypt(public, m):
    e, n = public
    c = ((m**e) % n)
    return c

def decrypt(private, encrypted_message):
    d, n = private
    m1 = ((encrypted_message**d) % n)
    return m1

def main():

    print "RSA Encrypter/ Decrypter"
    p = int(raw_input("Enter a prime number: "))
    q = int(raw_input("Enter a different prime number: "))
    print "-----------------------------"
    public, private = rsa(p, q)
    print "Public key = ", public
    # print "Private key = ", private
    print "-----------------------------"
    m = int(raw_input("Enter a message to encrypt: "))
    encrypted_message = encrypt(public, m)
    print "-----------------------------"
    print "The encrypted message is: ", encrypted_message
    print "-----------------------------"
    print "Decrypting with public key..."
    print "-----------------------------"
    decrypted_message = decrypt(private, encrypted_message)
    print "Decrypted message is: ", decrypted_message

if __name__ == "__main__":
    main()
