# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
import socket
from math import sqrt
import random
import secrets


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

# Get the hostname
hostn = socket.gethostname()
ipaddress = socket.gethostbyname(hostn)
# Get the full qualified domain name
fqdn = socket.getfqdn('www.google.com')
# Get the active network address
A_N_address = socket.gethostbyname_ex(hostn)

print('Hostname: '+hostn, ipaddress)
print('fqdn: '+fqdn)
print(A_N_address)

# Generating random IPv4
def randomip():
    first = random.randint(0,255)
    second = random.randint(0,255)
    third = random.randint(0,255)
    last = random.randint(0,255)
    iplist = f"{first}.{second}.{third}.{last}"
    print(iplist)
# Generating random MAC
def randomMAC():
    hexanum = (['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'])
    hexlist=[]
    for i in range(1,7):
        first = random.choice(hexanum)
        second = random.choice(hexanum)
        hexlist.append(first+second)
    macaddress = ":"
    print('MACAdress', macaddress.join(hexlist))

def randomIPv6():
    hexanum = (['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'])
    hexlist=[]
    for i in range(1,9):
        first = random.choice(hexanum)
        second = random.choice(hexanum)
        third = random.choice(hexanum)
        fourth = random.choice(hexanum)
        hexlist.append(first+second+third+fourth)
    ipv6address = ":"
    print('IPv6Adress', ipv6address.join(hexlist))



randomOddNumber(1, 10)

randomEvenNumber(11,20)
randomPrimeNumber(0,50)
randomip()
randomMAC()
randomIPv6()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
