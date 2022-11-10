



class DigitSumAlgorithm:
    pass
    @staticmethod
    def digitsum(dig =input('enter some digit to get the Sum: ')):
        sumd = 0
        dig=int(dig)
        while (dig > 0):
            i = dig % 10
            print(i)
            sumd = sumd + i
            dig = dig // 10
            print('digit', dig)
        print('Sum of Digits: ', sumd)
