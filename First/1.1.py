def isEven(value):
    a = bin(value)
    b = list(a)
    if int(b[-1])==0:
        return 'Четное'
    else:
        return 'Нечетное'

