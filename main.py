# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
from math import sqrt
import random

# random odd numbers in a range
def randomOddNumber(l, h):
    l = l // 2
    h = h // 2 - 1

    oddnum = random.randint(l, h)
    oddnum = (oddnum*2)+1
    print(oddnum)
# random even number in a range
def randomEvenNumber(el, eh):
    el = el // 2
    eh = eh // 2 - 1

    oddnum = random.randint(el, eh)
    oddnum = (oddnum * 2)
    print(oddnum)

# Prime number
def isPrime(n):
    if n==2 or n==3: return True
    if n<2 or n%2 == 0 or n%3 ==0: return False
    for k in range(5, int(sqrt(n)+1), 2):
        if n%k ==0:
            return False
    else:
        return True
# random prime number
def randomPrimeNumber(pl, ph):
# creating a list of prime numbers
    p = ([i for i in range(pl,ph) if isPrime(i)])
    pr = random.choice(p)
    print(pr)
















randomOddNumber(1, 10)

randomEvenNumber(11,20)
randomPrimeNumber(0,50)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
