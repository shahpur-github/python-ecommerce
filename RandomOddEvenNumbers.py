

import socket
from math import sqrt
import random
import secrets
class RandomOddEvenNumbers:
    pass
    @staticmethod
    # random odd numbers in a range
    def randomOddNumber(l, h):
        l = l // 2
        h = h // 2 - 1
        oddnum = random.randint(l, h)
        oddnum = (oddnum * 2) + 1
        print(oddnum)

    @staticmethod
    # random even number in a range
    def randomEvenNumber(el, eh):
        el = el // 2
        eh = eh // 2 - 1

        oddnum = random.randint(el, eh)
        oddnum = (oddnum * 2)
        print(oddnum)
        # random prime number

    @staticmethod
    def randomPrimeNumber(pl, ph):
        p = ([i for i in range(pl, ph) if isPrime(i)])
        pr = random.choice(p)
        print(pr)
    # Prime number



def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0 or n % 3 == 0: return False
    for k in range(5, int(sqrt(n) + 1), 2):
        if n % k == 0:
            return False
        else:
            return True


def Iseven(n):
    ev=n%2
    if ev ==0:
        return True
    else:
        return False

def Isodd(n):
    if (n%2) != 0:
        return True
    else:
        return False

