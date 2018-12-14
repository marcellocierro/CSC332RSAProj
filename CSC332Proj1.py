#!/usr/bin/python
import argparse
import sys
import random as random
from fractions import gcd
import math as math
import time as time
from memory_profiler import memory_usage

##################################################################################################################################
##################################################################################################################################
# Helper Methods
##################################################################################################################################
##################################################################################################################################
def options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p1', type = long, help = 'The size of the first prime to use; MUST BE 11,13,15,17')
    parser.add_argument('-p2', type = long, help = 'The size of the second prime to use; MUST BE 11,13,15,17')

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

def absoluteValue(p):
	if p>=0:
		p = p
	if p<0:
		p = -1 * p
	return p

def minimum(x,y):
	n = x
	if x>=y:
		n = x
	if y>x:
		n = y
	return n

def get_phi(p, q):
    phi = (p-1) * (q-1)
    return phi

def make_N(p, q):
    return p*q

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

#Standard Pollard Rho
def pollard_rho(n):
    provenFactors = []
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
            provenFactors.append(d)
            provenFactors.append(n/d)
            return provenFactors

#Pollard Rho brent Algo
def pollard_rho_brent(N):
	provenFactors = []

	if(N%2) == 0:
		return 2

	u = random.randint(1, N-1)
	h = random.randint(1, N-1)
	s = random.randint(1, N-1)
	i = 1
	k = 1
	q = 1

	while i == 1:
		x = u
		for j in range(k):
			u =((u*u)%N+k)%N
		f=0
		while f<k and i==1:
			yg = u
			for j in range(min(q,k-f)):
				u = ((u*u)%N+h)%N
				q = q * (absoluteValue(x-u))%N

			i = gcd(q,N)
			f = f+s
		k = k*2

	if i == N:
		while 0==0:
			yg = ((yg*yg)%N+h)%N
			i = gcd(absoluteValue(x-yg),N)
			if i>1:
				break

	provenFactors.append(i)
	provenFactors.append(N/provenFactors[0])

	return provenFactors

#Tree Factorization, Keep Going down by 2
def bruteForce_prime_factors(n):
    i = 2
    provenFactors = []
    while i**2 <= n:
        if n % i:
            i += 1
        else:
            n /= math.floor(i)
            provenFactors.append(i)
            provenFactors.append(n)

    return provenFactors

#Fermats, Returns List of Factors
def fermats(n):
    i = 0
    provenFactors = []
    while(True):
        t = math.ceil(math.sqrt(n)) + i
        s = math.sqrt((t**2) - n)
        i +=1
        if (s.is_integer() == True):
            p = t + s
            q = t - s

            provenFactors.append(p)
            provenFactors.append(q)
            #provenFactors.append((t+s))
            #provenFactors.append((t-s))
            return provenFactors
            break

def main():
    options()
    prime1 = options().p1
    prime2 = options().p2

    fivPrime = 48799
    sebPrime = 3727177
    ninPrime = 801236549
    elePrime = 98246064289
    thrPrime = 1012345678901
    fifPrime = 112582705942171
    sevPrime = 976543210123456789

    #p = 0
    #q = 0

    if prime1 == 5:
        p = fivPrime
    elif prime1 == 7:
        p = sebPrime
    elif prime1 == 9:
        p = ninPrime
    elif prime1 == 11:
        p = elePrime
    elif prime1 == 13:
        p = thrPrime
    elif prime1 == 15:
        p = fifPrime
    else:
        p = sevPrime

    if prime2 == 5:
        q = fivPrime
    elif prime2 == 7:
        q = sebPrime
    elif prime2 == 9:
        q = ninPrime
    elif prime2 == 11:
        q = elePrime
    elif prime2 == 13:
        q = thrPrime
    elif prime2 == 15:
        q = fifPrime
    else:
        q = sevPrime


    n = make_N(p, q)

    #n = 8051
    #n = 10834948153
    #n = 1923023412357
    #n = 9999999999973
    #n = 1231232134590149
    #n = 2778290744723171
    #n = 32193802514424469
    #n = 51923

    print "Factoring n: %s" % n

    ################## Pollard
    print 'Beginning Pollards Factorization, Tracking time and memory footprint'

    start_time = time.time()
    pollardFactors = pollard_rho(n)

    mem_usage = memory_usage((pollard_rho, (n,)))
    #print ('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
    print ('Maximum memory usage: %s' % max(mem_usage))
    print ('Total memory over cycle: %s' % sum(mem_usage))
    print pollardFactors

    elapsed_time = time.time() - start_time
    print time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

    ################## Pollard Rho Brent
    print 'Beginning Pollards Rho BRENT Factorization, Tracking time and memory footprint'

    start_time = time.time()
    pollardBrentFactors = pollard_rho_brent(n)

    mem_usage = memory_usage((pollard_rho_brent, (n,)))
    #print ('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
    print ('Maximum memory usage: %s' % max(mem_usage))
    print ('Total memory over cycle: %s' % sum(mem_usage))
    print pollardBrentFactors

    elapsed_time = time.time() - start_time
    print time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

    ################## Brute Force
    print 'Beginning Brute Force, Tracking time and memory footprint'

    start_time = time.time()
    bruteForceFactors = bruteForce_prime_factors(n)

    mem_usage = memory_usage((bruteForce_prime_factors, (n,)))
    #print ('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
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
    #print ('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
    print ('Maximum memory usage: %s' % max(mem_usage))
    print ('Total memory over cycle: %s' % sum(mem_usage))

    print pq

    elapsed_time = time.time() - start_time
    print time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

    #print message

if __name__ == "__main__":
    main()
