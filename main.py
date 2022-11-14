# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
import socket
from math import sqrt
import random
import secrets
import RandomOddEvenNumbers
import DigitSumAlgorithm


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
dumy = 0

#vard =DigitSumAlgorithm.DigitSumAlgorithm()
#vard.digitsum()
x='hello'[0]
print(x)

cvar = RandomOddEvenNumbers.RandomOddEvenNumbers()
print('from other class')
cvar.randomOddNumber(1,15)
cvar.randomPrimeNumber(1,10)

cvar.randomEvenNumber(11,20)

randomip()
randomMAC()
randomIPv6()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
