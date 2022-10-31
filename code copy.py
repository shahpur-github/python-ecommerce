
for y in range(x):
    if x <= 5:
        print(x, ' is less than or equal to 5')
    elif x <= 9:
        print(x,' is greater than or equal to 6')
    x = x -1


x=9
sum = 0

    for x in range(10):
        sum = x +1
        print(sum)
y=9
sum = 0
for x in range(y):
    y-=1
    sum =x+sum
    print(sum,y)


    def randomOddNumber(a, b):
        a = a // 2
        b = b // 2 - 1
        number = random.randint(a, b)
        number = (number * 2) + 1
        return number


    for i in range(pl, ph):
        pnum = random.randint(pl, ph)
        #print(pnum)
        if pnum == p[i]:
            print(pnum)
            break

    oddNumber = randomOddNumber(0, 100)
    print(oddNumber)