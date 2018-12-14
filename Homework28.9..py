#euclidian distance
from math import sqrt
x = [5, 6]
y = [8, 9]
distance = sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
print(distance)


def stat(v1,v2):
    answer = sqrt((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2)
    return answer

x = [5, 6]
y = [8, 9]
print (stat(x,y))



