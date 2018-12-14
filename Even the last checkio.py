import math
def even_last(V):
    a=len(V)
    if a==0:
        return ('0')
    else:
        list2=V[0::2]
        list3=sum(list2)*V[-1]
    return (list3)

data=[4]

print (even_last(data))
