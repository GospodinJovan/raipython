def checkio(number):
    string = str(number)
    product = 1
    for i in string:
        if int(i) !=0:
            product = product * int(i)
    return (product)

nombres=(2330)

print (checkio(nombres))

from functools import reduce

q=123405

print ((reduce(lambda x, y: x * y, (int(c) for c in str(q) if c != "0"), 1)))
