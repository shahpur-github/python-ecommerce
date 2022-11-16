import os

f = open('testcase1.txt', 'a')

f.write('this is the second line in the file \n ')
f.close()
f = open('testcase1.txt', 'r')
print(f.read())
#os.remove('testcase1.txt')

