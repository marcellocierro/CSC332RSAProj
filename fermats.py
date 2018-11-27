import math as math

def fermats(n):
    i = 0
    while(True):
        t = math.ceil(math.sqrt(n)) + i
        s = math.sqrt((t**2) - n)
        print "i: %s, t: %s, s: %s" % (i, t, s)
        i +=1
        if (s.is_integer() == True):
            break
def main():
    fermats(8051)

if __name__ == "__main__":
    main()



