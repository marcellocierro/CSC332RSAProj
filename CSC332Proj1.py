#!/usr/bin/python
import argparse
import sys
import random as random
from fractions import gcd
import math as math
import time as time
from memory_profiler import memory_usage

def options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-message', type = str, help = 'The Message to Encrpyt')

    args = parser.parse_args()
    return args

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

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

def pollard_rho(n):
    if n%2 == 0:
        return 2
    if is_prime(n):
        return n

    while True:
        c = random.randint(2, n-1)
        f = lambda x: x**2 + c
        x = y = 2
        d = 1
        while d == 1:
            x = f(x) % n
            y = f(f(y)) % n
            d = gcd((x-y) % n, n)
        if d!= n:
            return d

def bruteForce_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def fermats(n):
    i = 0
    while(True):
        t = math.ceil(math.sqrt(n)) + i
        s = math.sqrt((t**2) - n)
        print "i: %s, t: %s, s: %s" % (i, t, s)
        i +=1
        if (s.is_integer() == True):
            return ((t+s), (t-s))
            break

def get_phi(p, q):
    phi = (p-1) * (q-1)
    return phi

def main():
    options()
    message = options().message

    #n = 8051
    #n = 10834948153
    #n = 1923023412357
    #n = 9999999999973
    #n = 1231232134590149
    n = 32193802514424469
    #n = 51923

    ################## Pollard
    print 'Beginning Pollards Factorization, Tracking time and memory footprint'

    start_time = time.time()
    d = pollard_rho(n)
    p = d
    q = n/d

    mem_usage = memory_usage((pollard_rho, (n,)))
    print ('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
    print ('Maximum memory usage: %s' % max(mem_usage))
    print ('Total memory over cycle: %s' % sum(mem_usage))
    print p, q

    elapsed_time = time.time() - start_time
    print time.strftime("%H:%M:%S", time.gmtime(elapsed_time))


    ################## Brute Force
    print 'Beginning Brute Force, Tracking time and memory footprint'

    start_time = time.time()
    bruteForceFactors = bruteForce_prime_factors(n)

    mem_usage = memory_usage((bruteForce_prime_factors, (n,)))
    print ('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
    print ('Maximum memory usage: %s' % max(mem_usage))
    print ('Total memory over cycle: %s' % sum(mem_usage))

    print bruteForceFactors
    elapsed_time = time.time() - start_time
    print time.strftime("%H:%M:%S", time.gmtime(elapsed_time))


    ################## Fermats
    print 'Beginning Fermats, Tracking time and memory footprint'

    start_time = time.time()
    pq = fermats(n)

    mem_usage = memory_usage((fermats, (n,)))
    print ('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
    print ('Maximum memory usage: %s' % max(mem_usage))
    print ('Total memory over cycle: %s' % sum(mem_usage))

    print pq

    elapsed_time = time.time() - start_time
    print time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

    #print message

if __name__ == "__main__":
    main()

