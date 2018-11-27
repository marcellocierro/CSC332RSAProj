#!/usr/bin/python
import argparse
import sys
import math as math

def options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-modulus', type = int, help = 'The modulus')
    parser.add_argument('-number', type = int, help = 'The number')

    args = parser.parse_args()
    return args

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def main():

    options()
    modulus = options().modulus
    number = options().number

    print modinv(number, modulus)

if __name__ == "__main__":
    main()
