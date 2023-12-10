def isEven(value):
    a = list(bin(value))
    if int(a[-1])==0:
        return 'Четное'
    else:
        return 'Нечетное'

