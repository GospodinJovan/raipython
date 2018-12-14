v1=(16,7,3,5,18,19)
v2=sorted(v1)
v3=len(v2)
v4=((v3+1)/2)
print(v2)
print(v3)
print(v4)

import statistics
numbers = [16,7,3,5,18,19]
median = statistics.median(numbers)
print (median)


def stat(data):
    answer = statistics.median(data)
    return answer
numbers = [16,7,3,5,18,19]
print (stat(numbers))


import statistics
def median(l):
    a=len(l)
    if a == 0:
        raise Exception ("List is empty")
    elif a== 1:
        return l[0]
    s= sorted (l)
    if a % 2 == 0:
        return (s[a//2]+s[a//2-1])/2
    else:
        return s [a//2]

numbers = [16,7,3,5,18,19]
print (median(numbers))
