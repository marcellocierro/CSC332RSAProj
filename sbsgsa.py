#!/usr/bin/python
import math as math

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

def mk_list1(k, a, N):
    list1 = {}
    for i in range(k):
        if i != 0:
            list1[((a**i) % N)] = i
    return list1

def mk_list2(k, a, b, N):
    list2 = {}
    for i in range(k):
        if i != 0:
            list2[(b * (modinv(a, N) ** (i * k))) % N] = ((i * k),i)
    return list2

def main():
    #pick an arbitrary k, then follow shanks algorithm using the following parameters
    # a**x == b mod N

    k = 3
    a = 47
    b = 13
    N = 61

    #provide k, a, N
    list1 = mk_list1(k, a, N)

    #provide k, a, b, N
    list2 = mk_list2(k, a, b, N)

    potential_answers_list = []

    for key in list1:
        print "l1:", key, list1[key]

    for key in list2:
        print "l2:", key, list2[key]

    for key in list1:
        if key in list2:
            print "Key Match at: ", key, "With 'i'=", list1[key], "and 'mk'=", list2[key][0], "i2=", list2[key][1]
            potential_answers_list.append((list1[key] + list2[key][0]) % N)

    for element in potential_answers_list:
        if (((a**element) % N) == b):
            print element

if __name__ == "__main__":
    main()
