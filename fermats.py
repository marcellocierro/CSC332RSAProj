import math as math

def fermats(n):
    i = 0
    while(True):
        t = math.ceil(math.sqrt(n)) + i
        s = math.sqrt((t**2) - n)
        i +=1
        if (s.is_integer() == True):
            p = t - s
            q = t + s
            print p,q
            break
def main():
    fermats(366180471158482153)

if __name__ == "__main__":
    main()



