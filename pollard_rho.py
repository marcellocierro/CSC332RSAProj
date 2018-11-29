import random as random
from fractions import gcd
from memory_profiler import memory_usage

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

def main():
    #n = 8051
    #n = 10834948153
    n = 32193802514424469
    d = pollard_rho(n)
    mem_usage = memory_usage((pollard_rho, (n,)))
    print ('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
    print ('Maximum memory usage: %s' % max(mem_usage))
    print ('Total memory over cycle: %s' % sum(mem_usage))
    p = d
    q = (n/d)

    print p,q

if __name__ == "__main__":
    main()

