import math as math

def factors(n):
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def rsa(p, q):
    n = p * q

    g = factors(n)
    print g

    phi = (p-1) * (q-1)

    print "phi(n) = ", phi
    return phi

def main():
    p = int(raw_input("Enter a prime number: "))
    q = int(raw_input("Enter a different prime number: "))
    rsa(p,q)

if __name__ == "__main__":
    main()
